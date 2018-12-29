from app.db import db

from app.models import (  # noqa: F401
    room, player, card
)

db.create_all()
