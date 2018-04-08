from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Oi-qZaOE#YZ7_FTzvSBqhQP/ND}beRSjf!FbOdB8wHJsVD*VE-#G6+c]B^$3ria'
ALLOWED_HOSTS = ['andy-greenwell.org']

try:
    from .local import *
except ImportError:
    pass
