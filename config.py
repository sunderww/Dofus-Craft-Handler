
class BaseConfiguration(object):

    SECRET_KEY = 'MyAppSecret'
    DEBUG = False
    TESTING = False

    JWT_SECRET = 'MyJWTSecret'
    JWT_DEFAULT_ALGORITHM = 'HS512'
    JWT_AUTH_HEADER_PREFIX = 'JWT'
    JWT_IDENTITY_KEY = 'identity'
    JWT_ENV_KEY = 'JSON_WEB_TOKEN'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = True # Suppress warning

class DebugConfiguration(BaseConfiguration):
    DEBUG = True

class TestConfiguration(BaseConfiguration):
    TESTING = True
    SQLALCHEMY_ECHO = False # Force false to avoid thousands of lines of debug
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


def Config(app, **kwargs):
    app.url_map.strict_slashes = False

    if kwargs.get('debug', False):
        app.config.from_object(DebugConfiguration)
    else:
        app.config.from_object(BaseConfiguration)

    if kwargs.get('verbose', False):
        app.config['SQLALCHEMY_ECHO'] = True
