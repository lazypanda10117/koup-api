import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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

engine = create_engine(postgresURL, pool_recycle=7200)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
