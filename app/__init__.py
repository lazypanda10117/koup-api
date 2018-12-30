from flask import Flask
from flask_graphql import GraphQLView

# Declare application version.
version = "0.1.0"

# Initialize Flask app.
app = Flask(__name__)

from app import config  # noqa: F401
from app import routes  # noqa: F401
from app import schemas  # noqa: F401

app.add_url_rule( '/api', view_func=GraphQLView.as_view(
    'api',
    schema=schemas.schema,
    graphiql=True
))

if __name__ == '__main__':
    app.run(threaded=True, debug=True)
