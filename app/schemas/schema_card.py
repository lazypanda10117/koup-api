import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_card import ModelCard


class CardAttribute:
    name = graphene.String(description="Name of Card.")


class Card(SQLAlchemyObjectType, CardAttribute):
    class Meta:
        model = ModelCard
        interfaces = (graphene.relay.Node,)

