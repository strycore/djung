import os
from .base import *  # noqa

INSTALLED_APPS += (
    'devserver',
)

DEBUG = True

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),

        # It is strongly suggested to switch your dev environment's database
        # to the same engine as your production (PostgreSQL)
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': '{{ project_name }}',
        # 'USER': '{{ project_name }}',
        # 'PASSWORD': 'admin',
        # 'HOST': 'localhost'
    }
}
