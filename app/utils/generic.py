import app.utils.json as json
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


def query_object(cls, **kwargs):
    obj = db.session.query(cls).filter_by(**kwargs).all()
    return obj


def unique_integrity_check(cls, **kwargs):
    if len(query_object(cls, **kwargs)):
        error = "%s with unique attributes %s already exists." % (
            cls.__name__,
            json.dumps(kwargs)
        )
        raise SystemError(error)
