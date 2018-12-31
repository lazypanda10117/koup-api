import app.utils.datetime as datetime


def date_converter(obj):
    if isinstance(obj, datetime.datetime):
        return obj.__str__()
