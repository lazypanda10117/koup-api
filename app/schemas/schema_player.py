from random import shuffle
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType
import app.utils.graphqlUtil as gqlUtil
import app.utils.datetime as datetime
import app.utils.generic as generic
from app.models.model_player import ModelPlayer
from app.models.model_room import ModelRoom


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


class GetCardsInput(graphene.InputObjectType):
    id = graphene.ID(required=True, description="Global Id of the Player.")
    numCards = graphene.Int(required=True, default=2, description="Number of Cards to Get from Top of Draw Pile.")


class SwapAction:
    @staticmethod
    def setSwapping(room_id, swapping):
        room = generic.get_object(ModelRoom, dict(id=room_id))
        room_data = gqlUtil.serialize(room, ['players'])
        room_data['swapping'] = swapping
        generic.update_object(ModelRoom, room_data)


class GetCards(graphene.Mutation, SwapAction):
    @staticmethod
    def get_action(input):
        data = gqlUtil.input_to_dictionary(input)
        player = generic.get_object(ModelPlayer, data)
        player_data = gqlUtil.serialize(player)

        room = generic.get_object(ModelRoom, dict(id=player.room_id))
        room_data = gqlUtil.serialize(room, ['players'])

        get_hand = room.deck[:data['numCards']]

        player_data['hand'] = player.hand + get_hand
        room_data['deck'] = room.deck[data['numCards']:]
        room_data['last_update'] = datetime.datetime.utcnow()
        player = generic.update_object(ModelPlayer, player_data)
        generic.update_object(ModelRoom, room_data)
        return player

    player = graphene.Field(lambda: Player, description="Player updated by this mutation (get card).")

    class Arguments:
        input = GetCardsInput(required=True)

    def mutate(self, info, input):
        player = GetCards.get_action(input)
        GetCards.setSwapping(player.room_id, False)
        return GetCards(player=player)


class PutCardsInput(graphene.InputObjectType):
    id = graphene.ID(required=True, description="Global Id of the Player.")
    hand = graphene.List(graphene.Int, required=True, description="Cards to be Swapped")


class PutCards(graphene.Mutation, SwapAction):
    player = graphene.Field(lambda: Player, description="Player updated by this mutation (put card).")

    class Arguments:
        input = PutCardsInput(required=True)

    @staticmethod
    def putValidation(swapCards, selfCards, deck):
        for card in swapCards:
            if card in deck:
                err = "Card Already in Deck"
                raise SystemError(err)
            if card not in selfCards:
                err = "Card Swapped Does Not Belong to You."
                raise SystemError(err)

    @staticmethod
    def put_action(input):
        data = gqlUtil.input_to_dictionary(input)

        player = generic.get_object(ModelPlayer, data)
        player_data = gqlUtil.serialize(player)

        room = generic.get_object(ModelRoom, dict(id=player.room_id))
        room_data = gqlUtil.serialize(room)

        PutCards.putValidation(data['hand'], player.hand, room.deck)

        dumped_hand = data['hand']
        for card in dumped_hand:
            player_data['hand'].remove(card)

        room_data['deck'] = room.deck + dumped_hand
        shuffle(room_data['deck'])
        room_data['last_update'] = datetime.datetime.utcnow()

        player = generic.update_object(ModelPlayer, player_data)
        generic.update_object(ModelRoom, room_data)
        return player

    def mutate(self, info, input):
        player = PutCards.put_action(input)
        PutCards.setSwapping(player.room_id, False)
        return PutCards(player=player)


class RevealCards(graphene.Mutation):
    player = graphene.Field(lambda: Player, description="Player updated by this mutation (reveal card).")

    class Arguments:
        input = PutCardsInput(required=True)

    def mutate(self, info, input):
        data = gqlUtil.input_to_dictionary(input)
        PutCards.put_action(input)
        player = GetCards.get_action(GetCardsInput(id=data['id'], numCards=1))
        return RevealCards(player=player)

