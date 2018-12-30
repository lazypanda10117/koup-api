from app.db import Base
import enum
from app.utils.datetime import datetime
from app.models.func import Func
from app.models.model_player import ModelPlayer
from sqlalchemy import Column, Integer, String, ARRAY, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates


class GameState(enum.Enum):
    waiting = 1
    initializing = 2
    onGoing = 3


class ModelRoom(Base):
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    key = Column(String, nullable=False, unique=True)
    playerCap = Column(Integer, default=4, nullable=False)
    players = relationship("ModelPlayer", backref='room', lazy=True)
    deck = Column(ARRAY(Integer))
    state = Column(Enum(GameState), default=GameState.waiting)
    swapping = Column(Boolean, default=False)
    max_idle_time = Column(Integer, default=30)  # minutes
    last_update = Column(DateTime, nullable=False)

    def __init__(self, key, playerCap, deck, max_idle_time):
        self.key = key
        self.playerCap = playerCap
        self.deck = deck
        self.max_idle_time = max_idle_time
        self.last_update = datetime.now()
