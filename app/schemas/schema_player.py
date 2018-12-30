import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_player import ModelPlayer


class PlayerAttribute:
    hand = graphene.List(graphene.Int)
    room = graphene.ID(description="ID of Room that Player Belongs To.")


class Player(SQLAlchemyObjectType, PlayerAttribute):
    class Meta:
        model = ModelPlayer
        interfaces = (graphene.relay.Node,)

