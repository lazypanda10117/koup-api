from enum import IntEnum
from random import shuffle, randint
from sqlalchemy.orm import validates
from app.db import db
from app.models.func import Func
from app.models.model_card import ModelCard
import app.utils.generic as generic
import app.utils.datetime as datetime
import app.utils.converter as converter


class GameState(IntEnum):
    Waiting = 1
    Running = 2


class ModelRoom(db.Model, Func):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False, unique=True)
    player_cap = db.Column(db.Integer, default=4, nullable=False)
    players = db.relationship(
        'ModelPlayer',
        backref=db.backref('room', cascade='delete,all'),
        lazy=True,
        order_by='ModelPlayer.id'
    )
    deck = db.Column(db.ARRAY(db.Integer))
    state = db.Column(db.Integer, default=int(GameState.Waiting))
    swapping = db.Column(db.Boolean, default=False)
    rejoin = db.Column(db.Integer, default=0)
    max_idle_time = db.Column(db.Integer, default=30)  # minutes
    last_update = db.Column(db.DateTime, nullable=False)

    def __init__(
            self,
            key=0,
            player_cap=4,
            deck=list(range(15)),
            max_idle_time=30,
            last_update=datetime.datetime.utcnow()
    ):
        deck = [card.id for card in generic.query_object(ModelCard)]
        shuffle(deck)
        key = randint(1, 100001)
        super().__init__(
            key=key,
            player_cap=player_cap,
            deck=deck,
            max_idle_time=max_idle_time,
            last_update=last_update
        )

    def __repr_json__(self):
        return dict(
            id=self.id,
            key=self.key,
            player_cap=self.player_cap,
            players=self.players,
            deck=self.deck,
            state=self.state,
            swapping=self.swapping,
            max_idle_time=self.max_idle_time,
            last_update=converter.date_converter(self.last_update)
        )
