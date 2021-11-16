import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/tweeks'
    SECRET_KEY = '236d1ffbf7aa6933f300c626273e39ed'

class ProdConfig(Config):
    HEROKU_POSTGRESQL_AMBER_URL = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}