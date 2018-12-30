from app.db import Base
from app.models.func import Func
from sqlalchemy import Column, Integer, ARRAY, ForeignKey
from sqlalchemy.orm import validates


class ModelPlayer(Base, Func):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    hand = Column(ARRAY(Integer))
    room_id = Column(Integer, ForeignKey('room.id'), nullable=False)

    def __init__(self, hand, room):
        self.hand = hand
        self.room = room
