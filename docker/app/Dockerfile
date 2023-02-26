FROM python:3.10-slim-bullseye as image

FROM image as build-stage

ARG POETRY_VERSION=1.3.2
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

RUN apt-get update && apt-get upgrade -y
RUN apt-get install --no-install-recommends -y curl gcc musl-dev libffi-dev openssl
RUN pip3 install --no-cache-dir poetry==1.3.2
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

FROM build-stage as requirements
ARG APP_HOME=/app
WORKDIR ${APP_HOME}
RUN addgroup --system django && adduser --system --ingroup django django
COPY poetry.lock pyproject.toml ${APP_HOME}/
RUN poetry install --no-root $(test "$YOUR_ENV" == production && echo "--no-dev")

FROM requirements as install-app

COPY --chown=django:django . ${APP_HOME}
RUN chown django:django ${APP_HOME}

COPY --chown=django:django ./docker/app/entrypoint /entrypoint
COPY --chown=django:django ./docker/app/start /start-server
COPY --chown=django:django ./docker/app/celery/worker/start /start-celeryworker
COPY --chown=django:django ./docker/app/celery/beat/start /start-celerybeat
COPY --chown=django:django ./docker/app/celery/flower/start /start-flower

RUN sed -i 's/\r$//g' /entrypoint
RUN sed -i 's/\r$//g' /start-server
RUN sed -i 's/\r$//g' /start-celeryworker
RUN sed -i 's/\r$//g' /start-celerybeat
RUN sed -i 's/\r$//g' /start-flower

RUN chmod u+x /entrypoint
RUN chmod u+x /start-server
RUN chmod u+x /start-celeryworker
RUN chmod u+x /start-celerybeat
RUN chmod u+x /start-flower

USER django

FROM install-app as cqs
ENTRYPOINT ["/entrypoint"]
