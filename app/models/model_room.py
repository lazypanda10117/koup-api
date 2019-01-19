import string
from enum import IntEnum
from random import shuffle, choices
from sqlalchemy.orm import validates
from app import db
from app.models.func import Func
from app.models.model_card import ModelCard
import app.utils.generic as generic
import app.utils.datetime as datetime
import app.utils.converter as converter


class GameState(IntEnum):
    Waiting = 1
    Running = 2
    Rejoining = 3


class ModelRoom(db.Model, Func):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String, nullable=False, unique=True)
    player_cap = db.Column(db.Integer, default=6, nullable=False)
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

    def makeRoomKey(self, key):
        def autoRoomKey():
            def genAlphaNumKey(len):
                return ''.join(choices(string.ascii_uppercase + string.digits, k=len))

            while True:
                key = genAlphaNumKey(6)
                try:
                    generic.unique_integrity_check(self.__class__, key=key)
                    return key
                except SystemError as err:
                    print(err)

        def manualKey():
            generic.unique_integrity_check(self.__class__, key=key)
            return key

        return autoRoomKey() if key is None else manualKey()

    def __init__(
            self,
            key=None,
            player_cap=4,
            deck=list(),
            max_idle_time=30,
            last_update=datetime.datetime.utcnow()
    ):
        deck = [card.id for card in generic.query_object(ModelCard)]
        shuffle(deck)
        key = self.makeRoomKey(key)

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
