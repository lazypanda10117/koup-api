import os
import pytest
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#
# @pytest.fixture(scope='session')
# def app():
#     app = Flask(__name__)
#
#     user = os.environ.get("DB_USER", "")
#     password = os.environ.get("DB_PASS", "")
#     host = os.environ.get("DB_HOST", "")
#     port = os.environ.get("DB_PORT", "")
#     name = os.environ.get("DB_NAME", "")
#     postgresURL = os.environ.get("DATABASE_URL", "None")
#
#     if postgresURL == "None":
#         postgresURL = "postgresql://%s:%s@%s:%s/%s" % (
#             user, password, host, port, name
#         )
#
#     app.config["SQLALCHEMY_DATABASE_URI"] = postgresURL
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     app.config["SQLALCHEMY_POOL_RECYCLE"] = 7200
#
#     return app
#
#
# @pytest.fixture(scope='session')
# def _db(app):
#     db = SQLAlchemy(app=app)
#     return db
