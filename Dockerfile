FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y python-pip python-dev

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python web.py