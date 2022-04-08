from .settings import *
import os

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['NAME'],
        'HOST': 'localhost',
        'USER': os.environ['USER'],
        'PASSWORD': os.environ['PASSWORD']
    }
}
