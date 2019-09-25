FROM python:3.7-alpine

RUN pip install pip -U
RUN pip install flask requests

COPY app.py app.py
EXPOSE 5000:5000

ENTRYPOINT ["python", "app.py"]
