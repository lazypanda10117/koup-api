import json

# Declare shortcut to json.loads.
loads = json.loads


def encode(obj):
    if hasattr(obj, '__repr_json__'):
        return obj.__repr_json__()

    return json.JSONEncoder().default(obj)


def dumps(obj, **kw):
    return json.dumps(obj, default=encode, **kw)


def resp(data, code=200):
    return (
        dumps(data),
        code,
        {'Content-Type': 'application/json; charset=utf-8'}
    )


class IllegalJSONEncodeError(Exception):
    """
    This error indicates that a particular object should not be encoded as JSON.

    Any attempts to encode such an object should raise this exception.
    """

    object_class = None

    def __init__(self, obj):
        self.object_class = obj.__class__
        self.message = obj.__class__.__name__
