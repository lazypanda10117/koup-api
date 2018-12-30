from datetime import datetime

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
