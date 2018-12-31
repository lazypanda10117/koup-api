from app import app, version


@app.route("/", methods=["GET"])
def index():
    # from app.utils.setup import setup
    # setup()
    return "Koup Game API Version: % s" % version
