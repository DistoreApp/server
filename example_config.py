"""
!IMPORTANT!

This is the EXAMPLE config and WILL HAVE TO be 
renamed to config.py and edited correctly to work.

You can change which config to use based on how you
want the webserver to run, I think its pretty self
explanatory. You can also add new configs that change
different settings for the flask app. 

You can find a list of those here: 
https://flask.palletsprojects.com/en/1.1.x/config/#builtin-configuration-values
"""

class Config(object):
    TESTING = False
    DEBUG = False
    DATABASE = "postgres://username:password@localhost:5432/distore"
    TOKEN = "asdd"


class Production(Config):
    pass


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True
