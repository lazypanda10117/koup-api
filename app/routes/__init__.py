# Import models into app.db so that they are available for route functions.
from app import models  # noqa: E402, F401

from app.routes import (  # noqa:F401
    home, errors,

)
