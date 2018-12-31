from app.db import db
# from app.models.model_room import ModelRoom
# from app.models.model_player import ModelPlayer
from app.models.model_card import ModelCard


def setup():
    cardList = ['Duke', 'Contessa', 'Assassin', 'Ambassador', 'Captain']
    for card in cardList:
        for made in range(3):
            db.session.add(ModelCard(card))

    db.session.commit()
    db.session.close()
