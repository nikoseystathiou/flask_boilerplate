import os
from os import environ
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ENV
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SECRET_KEY = environ.get('SECRET_KEY')
    CSRF_ENABLED = True
    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('DB')
    SQLALCHEMY_ECHO = True
    # Flask-Security config
    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_HASH = environ.get('PASSWORD_HASH')
    SECURITY_PASSWORD_SALT = environ.get('PASSWORD_SALT')
    # Flask-Security URLs, overridden because they don't put a / at the end
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_REGISTER_URL = "/register/"
    SECURITY_POST_LOGIN_VIEW = '/admin/'
    SECURITY_POST_LOGOUT_VIEW = '/admin/'
    SECURITY_POST_REGISTER_VIEW = '/admin/'
    # Flask-Security features
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Template
    FLASK_ADMIN_SWATCH = 'sandstone'

class ProductionConfig(Config):
    DEBUG = True

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
