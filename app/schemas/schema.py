import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField
from .schema_card import Card, CardConnections, CreateCard, UpdateCard, DeleteCard
from .schema_player import Player, PlayerConnections, \
    CreatePlayer, UpdatePlayer, DeletePlayer, \
    PutCards, GetCards, RevealCards, \
    StartRoom, JoinRoom, JoinChecker
from .schema_room import Room, RoomNode, RoomConnections, CreateRoom, UpdateRoom, DeleteRoom, RestartRoom


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    card = relay.Node.Field(Card)
    allCards = SQLAlchemyConnectionField(CardConnections)
    player = relay.Node.Field(Player)
    allPlayers = SQLAlchemyConnectionField(PlayerConnections)
    room = RoomNode.Field(Room)
    allRooms = SQLAlchemyConnectionField(RoomConnections)


class Mutation(graphene.ObjectType):
    createCard = CreateCard.Field()
    updateCard = UpdateCard.Field()
    deleteCard = DeleteCard.Field()
    createPlayer = CreatePlayer.Field()
    updatePlayer = UpdatePlayer.Field()
    deletePlayer = DeletePlayer.Field()
    createRoom = CreateRoom.Field()
    updateRoom = UpdateRoom.Field()
    deleteRoom = DeleteRoom.Field()

    startRoom = StartRoom.Field()
    joinRoom = JoinRoom.Field()
    joinChecker = JoinChecker.Field()
    restartRoom = RestartRoom.Field()

    swapStart = GetCards.Field()
    swapEnd = PutCards.Field()
    revealCard = RevealCards.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[Card, Player, Room])
