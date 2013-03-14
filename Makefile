run:
	./manage.py runserver

db:
	./manage.py syncdb --noinput
	./manage.py migrate

test:
	./manage.py test

deps:
	pip install -r requirements.txt --exists-action=s --verbose

clean:
	find . -name "*.pyc" -delete

dumpfixtures:
	./manage.py dumpdata --indent=2 main > main/fixtures/initial_data.json

messages:
	django-admin.py makemessages -l fr_FR

compilemessages:
	django-admin.py compilemessages
