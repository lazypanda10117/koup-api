import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
import app.utils.graphqlUtil as gqlUtil
import app.utils.generic as generic
from app.models.model_card import ModelCard


class CardAttribute:
    type = graphene.String(description="Type of Card.")


class Card(SQLAlchemyObjectType, CardAttribute):
    class Meta:
        model = ModelCard
        model.db_id = model.id
        interfaces = (graphene.relay.Node,)

    db_id = graphene.Int()


class CardConnections(relay.Connection):
    class Meta:
        node = Card


class CreateCardInput(graphene.InputObjectType, CardAttribute):
    pass


class CreateCard(graphene.Mutation):
    card = graphene.Field(lambda: Card, description="Card created by this mutation.")

    class Arguments:
        input = CreateCardInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        card = generic.create_object(ModelCard, data)
        return CreateCard(card=card)


class UpdateCardInput(graphene.InputObjectType, CardAttribute):
    id = graphene.ID(required=True, description="Global Id of the Card.")


class UpdateCard(graphene.Mutation):
    card = graphene.Field(lambda: Card, description="Card updated by this mutation.")

    class Arguments:
        input = UpdateCardInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        card = generic.update_object(ModelCard, data)
        return UpdateCard(card=card)


class DeleteCard(graphene.Mutation):
    card = graphene.Field(lambda: Card, description="Card deleted by this mutation.")

    class Arguments:
        input = UpdateCardInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        card = generic.delete_object(ModelCard, data)
        return DeleteCard(card=card)
