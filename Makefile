vbin=venv/bin/

env:
	@echo '---------------------------------'
	@echo 'make virtualenv... please wait...'
	@echo '---------------------------------'
	virtualenv --no-site-packages venv
	@echo '---------------------------------'
	@echo 'install the python lib...please wait...'
	@echo '---------------------------------'
	$(vbin)pip install -r requirements.txt
	@echo '---------------------------------'
	@echo 'make env successfully!'
	@echo '----------------------------------'

initdb:
	@echo '---------------------------------'
	@echo 'init db... please wait...'
	@echo '---------------------------------'
	rm -r migrations/
	$(vbin)python manage.py db init
	$(vbin)python manage.py db migrate
	$(vbin)python manage.py db upgrade
	@echo '---------------------------------'
	@echo 'init db successfully!'
	@echo '----------------------------------'

syncdb:
	@echo '---------------------------------'
	@echo 'sync db... please wait...'
	@echo '---------------------------------'
	$(vbin)python manage.py db migrate
	$(vbin)python manage.py db upgrade
	@echo '---------------------------------'
	@echo 'sync db successfully!'
	@echo '----------------------------------'

demo:
	@echo '---------------------------------'
	@echo 'insert demo data to db... please wait...'
	@echo '---------------------------------'
	$(vbin)python manage.py demo
	@echo '---------------------------------'
	@echo 'insert demo data successfully!'
	@echo '----------------------------------'

run:
	$(vbin)python manage.py runserver

rung:
	$(vbin)gunicorn -w 5 -b 0.0.0.0:5000 manage:app

cleanenv:
	@echo 'clean the env...'
	rm -r venv/
	@echo 'clean successfully!'