from os import environ

DB_USER = environ.get("DB_USER", "review-sense")
DB_PASSWORD = environ.get("DB_PASSWORD", "review-sense")
DB_NAME = environ.get("DB_NAME", "review-sense")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_PORT = environ.get("DB_PORT", "5432")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)