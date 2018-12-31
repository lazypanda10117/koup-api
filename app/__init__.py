from flask import Flask
from flask_graphql import GraphQLView

# Declare application version.
version = "0.1.0"

# Initialize Flask app.
app = Flask(__name__)

from app import config  # noqa: F401
from app import routes  # noqa: F401
from app.schemas.schema import schema  # noga: F401


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('api', schema=schema, graphiql=True))

