import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app

user = os.environ.get("DB_USER", "robot")
password = os.environ.get("DB_PASS", "rootpwd")
host = os.environ.get("DB_HOST", "localhost")
port = os.environ.get("DB_PORT", "5432")
name = os.environ.get("DB_NAME", "koup")

postgresURL = os.environ.get("DATABASE_URL", "None")

if postgresURL == "None" :
    postgresURL = "postgresql://%s:%s@%s:%s/%s" % (
        user, password, host, port, name
    )

app.config["SQLALCHEMY_DATABASE_URI"] = postgresURL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_RECYCLE"] = 7200

db = SQLAlchemy(app)
migrate = Migrate(app, db)
