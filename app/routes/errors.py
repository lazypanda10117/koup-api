from werkzeug.exceptions import InternalServerError

from app import app


@app.errorhandler(InternalServerError)
def internal_server_error(error):
    return "An internal error occurred: %s" % error, 500
