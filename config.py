from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+pg8000://postgres:password@localhost/mydictionary",
)


class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    ENV = "production"


class DevelopmentConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True