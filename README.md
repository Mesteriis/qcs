# Test task for skypro

Code quality service aka test task for skypro

## Dependencies

- Poetry:

Install (Linux, macOS, Windows (WSL)):

``` bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows (Powershell):

``` powerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## Basic Commands

### Init local server

For local reversal, use the command

        $ make init

Local services will be started in a docker environment (postgres, redis), a poetry-based virtual environment will be
deployed, and a user avm q1w2e3w2e3 will be created

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "
  Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into
  your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

  ``` python
  python manage.py createsuperuser
  ```

  ``` bash
  make create_su_user
  ```

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar),
so that you can see how the site behaves for both kinds of users.

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd code_quality_service
celery -A config.celery_app worker -l info
```

or

``` bash
make start_local_celery
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the
same folder with *manage.py*, you should be right.
