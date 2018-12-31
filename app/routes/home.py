from app import app, version
from app.utils.setup import setup


@app.route("/", methods=["GET"])
def index():
    #setup()
    return "Koup Game API Version: % s" % version
