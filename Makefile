run:
	./manage.py runserver

setupenv:
	cp config/envvars ${VIRTUAL_ENV}/bin/postactivate

migrate:
	./manage.py migrate --noinput

test:
	./manage.py test

deps:
	pip install -r config/requirements/local.pip --exists-action=s
	npm install
	bower install

systemdeps:
	apt-get install -y postgresql libpq-dev python-dev supervisor nginx

clean:
	find . -name "*.pyc" -delete

dumpfixtures:
	./manage.py dumpdata --indent=2 core > core/fixtures/initial_data.json

messages:
	django-admin.py makemessages -l fr_FR

compilemessages:
	django-admin.py compilemessages

pylint:
	pylint --rcfile=config/pylintrc .

ctags:
	ctags -R --languages=python --python-kinds=-v ${VIRTUAL_ENV}/lib/python2.7
	ctags -R -a --languages=python --python-kinds=-v ${VIRTUAL_ENV}/src
	ctags -R -a --languages=python --python-kinds=-v .
