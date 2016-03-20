# -*- coding: utf-8 -*-
"""Application configuration."""
import os
from datetime import timedelta
from .constants import API_ENDPOINT
from decouple import config, Csv


class Config(object):
    """Base configuration."""

    SECRET_KEY = config('VWAUTH_SECRET', 'secret-key')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    #CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # db
    SQLALCHEMY_DATABASE_URI = config('VWAUTH_SQLALCHEMY_DATABASE_URI', 'sqlite:///{0}'.format('/db/dev.db'))

    # security
    SECURITY_REGISTERABLE = config('VWAUTH_SECURITY_REGISTERABLE', True)
    SECURITY_RECOVERABLE = config('VWAUTH_SECURITY_RECOVERABLE', True)
    SECURITY_TRACKABLE = config('VWAUTH_SECURITY_TRACKABLE', True)
    SECURITY_CONFIRMABLE = config('VWAUTH_SECURITY_CONFIRMABLE', True)
    SECURITY_PASSWORD_HASH = config('VWAUTH_SECURITY_PASSWORD_HASH', 'sha512_crypt')
    SECURITY_PASSWORD_SALT = config('VWAUTH_SECURITY_PASSWORD_SALT', 'add_salt')
    SECURITY_EMAIL_SENDER = config('VWAUTH_SECURITY_EMAIL_SENDER', 'welcome@virtualwatershed.org')

    # mail setting
    MAIL_SERVER = config('VWAUTH_MAIL_SERVER', None)
    MAIL_PORT = config('VWAUTH_MAIL_PORT', 25,cast=int)
    MAIL_USE_SSL = config('VWAUTH_MAIL_USE_SSL', False,cast=bool)
    MAIL_USERNAME = config('VWAUTH_MAIL_USERNAME', None)
    MAIL_PASSWORD = config('VWAUTH_MAIL_PASSWORD', None)


    # jwt
    JWT_EXPIRATION_DELTA = timedelta(days=config('VWAUTH_JWT_EXPIRATION_DELTA', 30,cast=int))
    JWT_AUTH_URL_RULE ='{base}/auth'.format(base=API_ENDPOINT)

    #CSRF
    WTF_CSRF_CHECK_DEFAULT = False
    #WTF_CSRF_ENABLED = False
class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    #DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format('/dev.db')
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    # WTF_CSRF_CHECK_DEFAULT = False

class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing