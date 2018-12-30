import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_room import ModelRoom


class Room(SQLAlchemyObjectType):
    class Meta:
        model = ModelRoom
        interfaces = (graphene.relay.Node,)


class RoomConnection(relay.Connection):
    class Meta:
        node = Room
