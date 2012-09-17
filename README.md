djung
=====

Boilerplate for Django projects

This boilerplate sets a standard Django project along with common components.
These components are:

- [Django Compressor](http://django_compressor.readthedocs.org/en/latest/index.html)
- [South](http://south.aeracode.org/)
- [Fabric](http://docs.fabfile.org)

Some frontend components are also shipped inside the project:
- [jQuery](http://jquery.com/)
- [Twitter Bootstrap](http://twitter.github.com/bootstrap/)
- [HTML5 Boilerplate](http://html5boilerplate.com/)

Reusable frontend components are installed with [bower](https://github.com/twitter/bower)
inside the 'components' folder.

Basic usage
-----------

You can quickly create a django project using this boilerplate with django-admin:

    django-admin.py startproject --template https://github.com/strycore/djung/zipball/master project_name

using grep find all the places containing "djung" and replace them with your project name

    grep -ri --exclude=README.md djung *

you can (and probably should) rename the example application using the same method:

    grep -r --exclude=README.md  frontend *



Note to other Django boilerplate authors: Please stop putting your Django apps
in a separate "apps" folder.
