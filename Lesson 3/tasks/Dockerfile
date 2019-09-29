FROM python:3.7-alpine

ARG APP_PORT

ENV APP_PORT ${APP_PORT:-5000}

WORKDIR /project/app

RUN pip install -U pip
RUN pip install python-json-logger
RUN pip install pipenv

COPY app.py app.py
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system

ENTRYPOINT flask run --host=0.0.0.0 --port=${APP_PORT}
