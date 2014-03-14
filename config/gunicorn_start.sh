#!/bin/bash

NAME="{{ project_name }}"
DJANGODIR=/srv/{{ project_name }}/project_name
SOCKFILE=/srv/{{ project_name }}/run/gunicorn.sock
USER=django
GROUP=django
NUM_WORKERS=9
DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
DJANGO_WSGI_MODULE={{ project_name }}.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
source ../bin/envvars

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name $NAME \
    --workers $NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --log-level=debug \
    --bind=unix:$SOCKFILE

