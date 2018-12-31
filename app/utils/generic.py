from app.db import db


def get_object(cls, data):
    id = data['id']
    queryCmd = (lambda id: db.session.query(cls).get(id))
    try:
        obj = queryCmd(id)
    except:
        print("Failed to get object")
        raise
    return obj


def create_object(cls, data):
    obj = cls(**data)
    db.session.add(obj)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        print("Failed to create object")
        raise
    return obj


def update_object(cls, data):
    id = data['id']
    queryCmd = (lambda id: db.session.query(cls).get(id))
    obj = queryCmd(id)
    print("data to be updataed: ")
    print(data)
    obj.update_from_dict(data)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        print("Failed to update object")
        raise
    return queryCmd(id)


def delete_object(cls, data):
    id = data['id']
    queryCmd = (lambda id: db.session.query(cls).get(id))
    obj = queryCmd(id)
    db.session.delete(obj)
    try:
        db.session.commit()
    except:
        db.session.rollback()
        print("Failed to delete object")
        raise
    return obj
