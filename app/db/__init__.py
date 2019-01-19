import os


def get_config_obj():
    user = os.environ.get("DB_USER", "")
    password = os.environ.get("DB_PASS", "")
    host = os.environ.get("DB_HOST", "")
    port = os.environ.get("DB_PORT", "")
    name = os.environ.get("DB_NAME", "")

    postgresURL = os.environ.get("DATABASE_URL", "None")

    if postgresURL == "None":
        postgresURL = "postgresql://%s:%s@%s:%s/%s" % (
            user, password, host, port, name
        )

    return dict(
        SQLALCHEMY_DATABASE_URI=postgresURL,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_POOL_RECYCLE=7200
    )

