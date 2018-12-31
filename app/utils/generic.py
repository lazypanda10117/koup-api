from app.db import db


def create_object(cls, data):
    obj = cls(**data)
    db.session.add(obj)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        print("Failed to update object")
        raise
    return obj


def update_object(cls, data):
    id = data['id']
    queryCmd = (lambda id: db.session.query(cls).get(id=id))
    obj = queryCmd(id)
    obj.update(data)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        print("Failed to update object")
        raise
    return queryCmd(id)
