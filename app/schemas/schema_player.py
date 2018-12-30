import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_player import ModelPlayer


class Player(SQLAlchemyObjectType):
    class Meta:
        model = ModelPlayer
        interfaces = (graphene.relay.Node,)


class PlayerConnection(relay.Connection):
    class Meta:
        node = Player
