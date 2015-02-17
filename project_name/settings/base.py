# -*- coding: utf-8 -*-
import os
import sys
from os.path import dirname, abspath

BASE_DIR= dirname(dirname(dirname(abspath(__file__))))
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Your Name', 'yourname@{{ project_name }}.com'),
)
MANAGERS = ADMINS
ROOT_URLCONF = '{{ project_name }}.urls'
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
SECRET_KEY = os.environ['SECRET_KEY']
ALLOWED_HOSTS = ('{{ project_name }}.strycore.com', )


# Apps
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
    'accounts',
)

# Localization
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static / Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

# Middleware
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Authentication / Users
AUTH_USER_MODEL = 'accounts.User'
ACCOUNT_ACTIVATION_DAYS = 3
LOGIN_REDIRECT_URL = "/"

# Email
DEFAULT_FROM_EMAIL = "admin@{{ project_name }}.com"
EMAIL_SUBJECT_PREFIX = "{{ project_name }}"

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'include_html': True,
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'syslog'],
            'level': 'ERROR',
        },
        'core': {
            'handlers': ['mail_admins', 'syslog'],
            'level': 'ERROR',
        },
        'accounts': {
            'handlers': ['mail_admins', 'syslog'],
            'level': 'ERROR',
        },
    }
}

if "test" in sys.argv:
    CELERY_ALWAYS_EAGER = True
    CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

CELERY_SEND_TASK_ERROR_EMAILS = True
BROKER_URL = 'amqp://guest:guest@localhost//'
