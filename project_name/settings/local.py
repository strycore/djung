from .base import *  # noqa

INSTALLED_APPS += (
    'devserver',
)

DEBUG = True

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    }
}
