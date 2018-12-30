import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model_room import ModelRoom


class RoomAttribute:
    key = graphene.String(description="Key of Room.")
    playerCap = graphene.Int(descrption="Max Capacity of Room.")
    deck = graphene.List(graphene.Int)
    state = graphene.Int(description="Game State.")
    swapping = graphene.Boolean(description="Swapping State of Game.")
    max_idle_time = graphene.Int(description="Max Allowed Idle Minutes.")
    last_update = graphene.DateTime(description="Time of Last Invoked Action.")


class Room(SQLAlchemyObjectType, RoomAttribute):
    class Meta:
        model = ModelRoom
        interfaces = (graphene.relay.Node,)

