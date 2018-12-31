from app.db import db
from enum import IntEnum
import app.utils.datetime as datetime
from app.models.func import Func
from sqlalchemy.orm import validates


class GameState(IntEnum):
    Waiting = 1
    Initializing = 2
    Running = 3


class ModelRoom(db.Model, Func):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False, unique=True)
    player_cap = db.Column(db.Integer, default=4, nullable=False)
    players = db.relationship(
        'ModelPlayer',
        backref='room',
        cascade='delete,all',
        lazy=True,
        order_by='ModelPlayer.id'
    )
    deck = db.Column(db.ARRAY(db.Integer))
    state = db.Column(db.Integer, default=int(GameState.Waiting))
    swapping = db.Column(db.Boolean, default=False)
    max_idle_time = db.Column(db.Integer, default=30)  # minutes
    last_update = db.Column(db.DateTime, nullable=False)

    def __init__(
            self,
            key,
            player_cap=4,
            deck=range(15),
            max_idle_time=30,
            last_update=datetime.datetime.utcnow()
    ):
        super().__init__(
            key=key,
            player_cap=player_cap,
            deck=deck,
            max_idle_time=max_idle_time,
            last_update=last_update
        )
