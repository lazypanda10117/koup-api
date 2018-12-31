from app.db import db
from app.models.func import Func
from sqlalchemy.orm import validates


class ModelCard(db.Model, Func):
    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        super().__init__(
            name=name
        )

    def __repr_json__(self):
        return dict(
            id=self.id,
            name=self.name
        )
