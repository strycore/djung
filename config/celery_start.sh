#!/bin/bash

DJANGODIR=/srv/{{ project_name }}/{{ project_name }}
DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production

cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
source ../bin/envvars

exec ../bin/celery worker -A {{ project_name }}.celery.app --loglevel=INFO
