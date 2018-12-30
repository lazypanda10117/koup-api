from app.db import Session, engine, Base
# from app.models.model_room import ModelRoom
# from app.models.model_player import ModelPlayer
from app.models.model_card import ModelCard

Base.metadata.create_all(engine)

session = Session()
cardList = ['Duke', 'Contessa', 'Assassin', 'Ambassador', 'Captain']
for card in cardList:
    for made in range(3):
        session.add(ModelCard(card))

session.commit()
session.close()
