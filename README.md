djung
=====

Boilerplate for Django projects

This boilerplate sets a standard Django project along with common components.
These components are:

- [Fabric](http://docs.fabfile.org): Website deployment
- [Celery](http://www.celeryproject.org/): Async and distributed task queue

On the server, the project is configured by default to use:
- [Nginx](http://nginx.com)
- [PostgreSQL](http://www.postgresql.org/)
- [Supervisor](http://supervisord.org/)
- [Gunicorn](http://gunicorn.org/)


Basic usage
-----------

You can quickly create a django project using this boilerplate with django-admin:

    django-admin.py startproject --template https://github.com/strycore/djung/zipball/master project_name

Oneliner to create a project and push it to your staging server (assumes you
have cloned the repository and changed the domain in fabfile.py)

    mkvirtualenv -i django foo; django-admin.py startproject --template djung foo; cd foo; fab staging setup; fab staging deploy

Running the project
-------------------

Like most production-ready Django project, Djung has several settings files you
can use. It currently ships with two different settings: one for local
development and one for production. To use one or the other, set the
DJANGO_SETTINGS_MODULE environment varible to the appropriate settings module:

    export DJANGO_SETTINGS_MODULE=myproject.settings.local

Typing this command will get really old really fast if you have to do it each
time you work on your project so it's recommended to add this line to
~/.virtualenvs/myproject/bin/postactivate

Do not forget to set the SECRET_KEY as well in your environment variables.
For your convienience, you can use the file config/envvars as your postactivate
script or in your production setup.
