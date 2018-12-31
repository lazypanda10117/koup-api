from app.db import db
from app.models.func import Func
from sqlalchemy.orm import validates


class ModelPlayer(db.Model, Func):
    __tablename__ = "player"

    id = db.Column(db.Integer, primary_key=True)
    hand = db.Column(db.ARRAY(db.Integer))
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)

    def __init__(self, hand, room_id):
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
