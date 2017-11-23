import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """Common config"""
    SECRET_KEY="MY_SECRET_KEY"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    DEBUG=True
    # SQLALCHEMY_DATABASE_URI= os.environ['DATABASE_URL']
    # SQLALCHEMY_DATABASE_URI="postgres://postgres:root@localhost:5432/blog_app"
    SQLALCHEMY_DATABASE_URI="postgres://postgres:root@db_postgres:5432/postgres"

class ProdConfig(Config):
    DEBUG=False

class TestConfig(Config):
    TESTING=True
    WTF_CSRF_ENABLED=False
    SQLALCHEMY_DATABASE_URI="postgres://postgres:root@localhost:5432/blog_app_test"
