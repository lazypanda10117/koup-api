from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db import get_config_obj

# Declare application version.
version = "0.1.0"

# Initialize Flask app.
def create_app(name_handler, config_object):
    def config_parser(app, obj):
        for key, data in obj.items():
            app.config[key] = data
    app = Flask(name_handler)
    config_parser(app, config_object)
    return app


app = create_app(__name__, get_config_obj())
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app, resources={r"/graphql/*": {"origins": "*"}})

from app import config  # noqa: F401
from app import routes  # noqa: F401
from app.schemas.schema import schema  # noga: F401

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('api', schema=schema, graphiql=True))
