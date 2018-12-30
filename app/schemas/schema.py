import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType, utils
from .schema_card import Card, CardConnection
from .schema_player import Player, PlayerConnection
from .schema_room import Room, RoomConnection


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    card = relay.Node.Field(Card)
    all_cards = SQLAlchemyConnectionField(CardConnection)


schema = graphene.Schema(query=Query, types=[Card])
