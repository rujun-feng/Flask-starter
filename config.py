# coding: utf-8

class BaseConfig:
    """
    Plz change SQLALCHEMY_DATABASE_URI to your production database
    Support for most relational databases
    """
    DEBUG = True
    SECRET_KEY = '%123456'
    SQLALCHEMY_DATABASE_URI = 'xxx'


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/flaskstarter?charset=utf8'


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/flaskstarter?charset=utf8'


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/flaskstarter?charset=utf8'


config = {
    'Local': LocalConfig,
    'Dev': DevelopmentConfig,
    'Prd': ProductionConfig,
}