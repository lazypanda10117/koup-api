from sqlalchemy.orm import validates
from app.db import db
from app.models.func import Func


class ModelPlayer(db.Model, Func):
    __tablename__ = "player"

    id = db.Column(db.Integer, primary_key=True)
    hand = db.Column(db.ARRAY(db.Integer))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))

    def __init__(self, room_id, hand=[]):
        super().__init__(
            hand=hand,
            room_id=room_id
        )

    def __repr_json__(self):
        return dict(
            id=self.id,
            hand=self.hand,
            room_id=self.room_id
        )
