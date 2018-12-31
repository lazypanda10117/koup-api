from datetime import datetime, timedelta

DATETIME_FORMAT = "%d/%m/%Y %I:%M:%S %p"


def format_datetime(dt):
    """
    Formats the datetime 'val' as a string.
    """
    return dt.strftime(DATETIME_FORMAT)


def parse_time(time_str):
    """
    Parses a time string into a datetime.
    """
    return datetime.strptime(time_str, DATETIME_FORMAT)


def time_back(minutes):
    return datetime.utcnow() - timedelta(minutes=minutes)
