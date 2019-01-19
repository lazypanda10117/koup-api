from sqlalchemy.orm import validates
from app import db
from app.models.func import Func


class ModelCard(db.Model, Func):
    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)

    def __init__(self, type):
        super().__init__(
            type=type
        )

    def __repr_json__(self):
        return dict(
            id=self.id,
            type=self.type
        )
