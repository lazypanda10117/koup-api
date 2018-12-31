import graphene
import app.utils.graphqlUtil as gqlUtil
import app.utils.generic as generic
import app.utils.datetime as datetime
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_room import ModelRoom


class RoomAttribute:
    key = graphene.String(description="Key of Room.")
    player_cap = graphene.Int(descrption="Max Capacity of Room.")
    deck = graphene.List(graphene.Int)
    state = graphene.Int(description="Game State.")
    swapping = graphene.Boolean(description="Swapping State of Game.")
    max_idle_time = graphene.Int(description="Max Allowed Idle Minutes.")
    last_update = graphene.DateTime(description="Time of Last Invoked Action.")


class Room(SQLAlchemyObjectType):
    class Meta:
        model = ModelRoom
        interfaces = (graphene.relay.Node,)


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
