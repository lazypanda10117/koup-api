from app import app, version


@app.route("/", methods=["GET"])
def index():
    return "Koup Game API Version: % s" % version
