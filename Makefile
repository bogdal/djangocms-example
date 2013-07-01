SETTINGS = project.settings

install:
	pip install -r deploy/requirements.txt

init: install
	mkdir static -p
	mkdir media -p

	@DJANGO_SETTINGS_MODULE=$(SETTINGS) python manage.py syncdb --all
	@DJANGO_SETTINGS_MODULE=$(SETTINGS) python manage.py migrate --fake