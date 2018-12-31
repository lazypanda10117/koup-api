from app.db import db
# from app.models.model_room import ModelRoom
# from app.models.model_player import ModelPlayer
from app.models.model_card import ModelCard


def setup():
    if not db.session.query(ModelCard).count():
        cardList = ['Duke', 'Contessa', 'Assassin', 'Ambassador', 'Captain']
        for card in cardList:
            for made in range(3):
                db.session.add(ModelCard(card))
        db.session.commit()
    else:
        raise SystemError('You Have Already Setup the Koup API.')
