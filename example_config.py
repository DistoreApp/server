class Config(object):
    TESTING = False
    DEBUG = False
    DATABASE = "postgres://username:password@localhost:5432/distore"


class Production(Config):
    pass


class Development(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True