FROM python:3.7-alpine

WORKDIR /home/volerij/Project

RUN pip install -U pip
RUN pip install pipenv

COPY app.py app.py
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system

ARG APP_PORT
ENV APP_PORT ${APP_PORT:-5000}

ENTRYPOINT flask run --host=0.0.0.0 --port=${APP_PORT}

