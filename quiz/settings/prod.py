import os
from .settings import *

ALLOWED_HOSTS = []
DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['NAME'],
        'HOST': 'localhost',
        'USER': os.environ['USERNAME'],
        'PASSWORD': os.environ['PASSWORD']
    }
}

STATIC_ROOT = '/home/optimal1/public_html/static'