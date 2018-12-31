import graphene
from graphene import relay
import app.utils.graphqlUtil as gqlUtil
import app.utils.generic as generic
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_player import ModelPlayer


class PlayerAttribute:
    hand = graphene.List(graphene.Int)
    room_id = graphene.ID(description="ID of Room that Player Belongs To.")


class Player(SQLAlchemyObjectType, PlayerAttribute):
    class Meta:
        model = ModelPlayer
        interfaces = (graphene.relay.Node,)


class PlayerConnections(relay.Connection):
    class Meta:
        node = Player


class CreatePlayerInput(graphene.InputObjectType, PlayerAttribute):
    pass


class CreatePlayer(graphene.Mutation):
    player = graphene.Field(lambda: Player, description="Player created by this mutation.")

    class Arguments:
        input = CreatePlayerInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        player = generic.create_object(ModelPlayer, data)
        return CreatePlayer(player=player)


class UpdatePlayerInput(graphene.InputObjectType, PlayerAttribute):
    id = graphene.ID(required=True, description="Global Id of the Player.")


class UpdatePlayer(graphene.Mutation):
    player = graphene.Field(lambda: Player, description="Player updated by this mutation.")

    class Arguments:
        input = UpdatePlayerInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        player = generic.update_object(ModelPlayer, data)
        return UpdatePlayer(player=player)


class DeletePlayer(graphene.Mutation):
    player = graphene.Field(lambda: Player, description="Player deleted by this mutation.")

    class Arguments:
        input = UpdatePlayerInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        player = generic.delete_object(ModelPlayer, data)
        return DeletePlayer(player=player)
