from app import app, version


@app.route("/", methods=["GET"])
def index():
    return "Koup Game API Version: % s" % version


@app.route("/setup", methods=["GET"])
def setup():
    from app.utils.setup import setup
    setup()
    return "Successfully Set Up API"
