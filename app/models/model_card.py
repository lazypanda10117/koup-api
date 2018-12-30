from app.db import Base
from app.models.func import Func
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


class ModelCard(Base, Func):
    __tablename__ = "card"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __init__(self, name):
        self.name = name
