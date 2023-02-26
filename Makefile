init:
	make start_local_services
	poetry install
	make make_migrations_migrate
	make create_su_user
	make load_fixtures
	make run_server

start_local_services:
	docker-compose -f ./local.yml up -d db redis

start_local_celery:
	docker-compose -f ./local.yml up -d celeryworker celerybeat flower

make_migrations_migrate:
	DJANGO_SETTINGS_MODULE=config.settings.dev poetry run ./manage.py makemigrations
	DJANGO_SETTINGS_MODULE=config.settings.dev poetry run ./manage.py migrate

create_su_user:
	DJANGO_SETTINGS_MODULE=config.settings.dev DJANGO_SUPERUSER_USERNAME="avm" DJANGO_SUPERUSER_PASSWORD="q1w2e3w2e3" DJANGO_SUPERUSER_EMAIL="avm@sh-inc.ru" poetry run ./manage.py createsuperuser --noinput

load_fixtures:
	DJANGO_SETTINGS_MODULE=config.settings.dev poetry run ./manage.py loaddata ./fixtures/tasks.json

generate_key:
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./keys/ssl/selfsigned.key -out ./keys/ssl/selfsigned.crt

run_server:
	DJANGO_SETTINGS_MODULE=config.settings.dev poetry run ./manage.py runserver

run_server_ssl:
	DJANGO_SETTINGS_MODULE=config.settings.dev poetry run daphne -e ssl:8000:privateKey=./keys/ssl/selfsigned.key:certKey=./keys/ssl/selfsigned.crt config.asgi:application

run_server_docker:
	docker-compose -f local.yml up --build django
