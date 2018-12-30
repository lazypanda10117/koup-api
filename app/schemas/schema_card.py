import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_card import ModelCard


class Card(SQLAlchemyObjectType):
    class Meta:
        model = ModelCard
        interfaces = (graphene.relay.Node,)


class CardConnection(relay.Connection):
    class Meta:
        node = Card
