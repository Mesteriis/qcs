init:
	poetry install
	make start_local_services
	make make_migrations_migrate
	make load_fixtures
	make generate_key
	make run_server_ssl

test:
	poetry run pytest

start_local_services:
	docker-compose -f ./local.yml up -d db redis

start_local_celery:
	docker-compose -f ./local.yml up -d celeryworker celerybeat flower

dell_all_migration:
	find ./app -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find ./app -path "*/migrations/*.pyc" -delete

make_migrations_migrate:
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run ./manage.py makemigrations
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run ./manage.py migrate
	DJANGO_SETTINGS_MODULE=config.settings.local DJANGO_SUPERUSER_USERNAME="avm" DJANGO_SUPERUSER_PASSWORD="q1w2e3w2e3" DJANGO_SUPERUSER_EMAIL="avm@sh-inc.ru" poetry run ./manage.py createsuperuser --noinput

save_fixtures:
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run  ./manage.py dumpdata imap_transport.MailService --indent 4 > ./fixtures/mail_service.json
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run  ./manage.py dumpdata emailbox.Mailbox --indent 4 > ./fixtures/emailbox.json
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run  ./manage.py dumpdata third_party_systems.Credentials --indent 4 > ./fixtures/сredentials.json
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run  ./manage.py dumpdata third_party_systems.ThirdPartySystem --indent 4 > ./fixtures/tpsystem.json

load_fixtures:
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run ./manage.py loaddata ./fixtures/mail_service.json
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run ./manage.py loaddata ./fixtures/emailbox.json
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run ./manage.py loaddata ./fixtures/tpsystem.json
	DJANGO_SETTINGS_MODULE=config.settings.local poetry run ./manage.py loaddata ./fixtures/сredentials.json

recreate_db:
	make dell_all_migration
	rm -Rf ./media/attachment/*
	rm -Rf ./media/avatars/*
	make make_migrations_migrate
	make load_fixtures

generate_key:
	openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./keys/ssl/selfsigned.key -out ./keys/ssl/selfsigned.crt

run_server_ssl:
	DJANGO_SETTINGS_MODULE=config.settings.dev poetry run daphne -e ssl:8000:privateKey=./keys/ssl/selfsigned.key:certKey=./keys/ssl/selfsigned.crt config.asgi:application

run_server_docker:
	docker-compose -f local.yml up --build django
