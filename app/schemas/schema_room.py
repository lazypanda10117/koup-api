from random import shuffle
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
import app.utils.graphqlUtil as gqlUtil
import app.utils.generic as generic
import app.utils.datetime as datetime
from app.models.model_room import ModelRoom, GameState
from app.models.model_player import ModelPlayer
from app.models.model_card import ModelCard


class RoomAttribute:
    key = graphene.String(description="Key of Room.")
    player_cap = graphene.Int(descrption="Max Capacity of Room.")
    deck = graphene.List(graphene.Int)
    state = graphene.Int(description="Game State.")
    swapping = graphene.Boolean(description="Swapping State of Game.")
    max_idle_time = graphene.Int(description="Max Allowed Idle Minutes.")
    last_update = graphene.DateTime(description="Time of Last Invoked Action.")


class RoomNode(relay.Node):
    class Meta:
        name = 'RoomNode'

    @classmethod
    def get_node_from_global_id(cls, info, global_id, only_type=None):
        room = generic.query_object(ModelRoom, key=global_id)
        if not room:
            raise Exception("No matching Global ID with Given Key")
        global_decoded_id = super().to_global_id(only_type._meta.name, room[0].id)
        return super().get_node_from_global_id(info, global_decoded_id, only_type)


class Room(SQLAlchemyObjectType):
    class Meta:
        model = ModelRoom
        interfaces = (RoomNode,)


class RoomConnections(relay.Connection):
    class Meta:
        node = Room


class CreateRoomInput(graphene.InputObjectType, RoomAttribute):
    pass


class CreateRoom(graphene.Mutation):
    room = graphene.Field(lambda: Room, description="Room created by this mutation.")

    class Arguments:
        input = CreateRoomInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        data['last_update'] = datetime.datetime.utcnow()
        room = generic.create_object(ModelRoom, data)
        return CreateRoom(room=room)


class UpdateRoomInput(graphene.InputObjectType, RoomAttribute):
    id = graphene.ID(required=True, description="Global Id of the Room.")


class UpdateRoom(graphene.Mutation):
    room = graphene.Field(lambda: Room, description="Room updated by this mutation.")

    class Arguments:
        input = UpdateRoomInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        data['last_update'] = datetime.datetime.utcnow()
        room = generic.update_object(ModelRoom, data)
        return UpdateRoom(room=room)


class DeleteRoom(graphene.Mutation):
    room = graphene.Field(lambda: Room, description="Room deleted by this mutation.")

    class Arguments:
        input = UpdateRoomInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        room = generic.delete_object(ModelRoom, data)
        return DeleteRoom(room=room)


class RestartRoomInput(graphene.InputObjectType, RoomAttribute):
    key = graphene.ID(required=True, description="Key of the Room.")


class RestartRoom(graphene.Mutation):
    room = graphene.Field(lambda: Room, description="Room updated by this mutation (restart room).")

    class Arguments:
        input = RestartRoomInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)

        player_count = 0
        for player in generic.query_object(ModelRoom, key=data['key']):
            generic.delete_object(ModelPlayer, gqlUtil.serialize(player))
            player_count += 1

        room = generic.get_object(ModelRoom, dict(key=data['key']))
        room_data = gqlUtil.serialize(room)

        new_deck = [card.id for card in generic.query_object(ModelCard)]
        shuffle(new_deck)

        room_data['deck'] = new_deck
        room_data['state'] = int(GameState.Rejoining)
        room_data['swapping'] = False
        room_data['rejoin'] = player_count
        room_data['last_update'] = datetime.datetime.utcnow()
        room = generic.update_object(ModelRoom, room_data)

        return RestartRoom(room=room)
