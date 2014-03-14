djung
=====

Boilerplate for Django projects

This boilerplate sets a standard Django project along with common components.
These components are:

- [South](http://south.aeracode.org/): Database migrations
- [Fabric](http://docs.fabfile.org): Website deployment
- [Celery](http://www.celeryproject.org/): Async and distributed task queue
- [Nose](https://nose.readthedocs.org/en/latest/): Test framework

Frontend libraries are available with [bower](https://github.com/twitter/bower):
- [jQuery](http://jquery.com/)
- [Twitter Bootstrap](http://twitter.github.com/bootstrap/)
- [Modernizr](http://modernizr.com/)

To install them, run `bower install`.

Djung uses Grunt to compile and minify css and js. It is configured for use
with livereload which you can enable by running `grunt watch`

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

