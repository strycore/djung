import os
from .base import *  # noqa

DEBUG = False

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': 'localhost'
    }
}

SECRET_KEY = os.environ['SECRET_KEY']
