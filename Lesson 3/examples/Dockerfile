FROM python:3.7-alpine

WORKDIR /var/app

RUN pip install -U pip
RUN pip install python-json-logger

COPY app.py app.py
COPY file.txt file.txt

ENTRYPOINT ["python", "app.py"]
