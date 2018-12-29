from flask import Flask
from flask_graphql import GraphQLView

# Declare application version.
version = "0.1.0"

# Initialize Flask app.
app = Flask(__name__)

# Configure Flask.
from app import config  # noqa: F401

# Import all routes so that they are registered in Flask.
from app import routes  # noqa: F401
