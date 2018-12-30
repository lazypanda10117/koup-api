import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
import app.schemas.schema_room as room
import app.schemas.schema_player as player
import app.schemas.schema_card as card


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    room = graphene.relay.Node.Field(room.Room)
    roomList = SQLAlchemyConnectionField(room.Room)
    player = graphene.relay.Node.Field(player.Player)
    playerList = SQLAlchemyConnectionField(player.Player)
    card = graphene.relay.Node.Field(card.Card)
    cardList = SQLAlchemyConnectionField(card.Card)


schema = graphene.Schema(query=Query)
