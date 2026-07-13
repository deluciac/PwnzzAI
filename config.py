import os

_BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def _sqlite_uri(path: str) -> str:
    return "sqlite:///" + os.path.normpath(path).replace("\\", "/")


# Same directory as the main shop DB (pizza_shop.db): no extra folder required.
_DEFAULT_CATERING_SQL_URI = _sqlite_uri(os.path.join(_BASE_DIR, "catering_sql_lab.db"))
_CATERING_SQL_DATABASE_URI = os.environ.get("CATERING_SQL_DATABASE_URI", _DEFAULT_CATERING_SQL_URI)
_DEVELOPMENT_SECRET_KEY = "dev-secret-key-change-in-production"


def _secret_key() -> str:
    environment = os.environ.get("FLASK_ENV", "").strip().lower()
    configured_key = os.environ.get("SECRET_KEY")

    if environment == "development":
        return configured_key or _DEVELOPMENT_SECRET_KEY

    if (
        not configured_key
        or configured_key == _DEVELOPMENT_SECRET_KEY
        or len(configured_key.encode("utf-8")) < 32
    ):
        raise RuntimeError(
            "SECRET_KEY must be supplied externally and contain at least 32 bytes "
            "outside development"
        )
    return configured_key


class Config(object):

    # Main shop database (pizzas, users, comments, orders)
    SQLALCHEMY_DATABASE_URI = "sqlite:///pizza_shop.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Isolated SQLite DB for the catering agentic SQL / tool lab only (routing_flag)
    CATERING_SQL_DATABASE_URI = _CATERING_SQL_DATABASE_URI
    SQLALCHEMY_BINDS = {
        "catering_sql": _CATERING_SQL_DATABASE_URI,
    }

    # Secret key for session management
    SECRET_KEY = _secret_key()
