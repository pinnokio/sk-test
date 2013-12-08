PROJECT_DIR=$(PWD)/students

devserver:
	$(PROJECT_DIR)/manage.py runserver

syncdb:
	$(PROJECT_DIR)/manage.py syncdb

syncdb-silent:
	$(PROJECT_DIR)/manage.py syncdb --noinput