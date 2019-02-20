FROM ubuntu:18.04

MAINTAINER "Sid Ramesh"

COPY ./ ./Anagramic

WORKDIR ./Anagramic

RUN apt-get update
RUN apt-get install git -y
RUN apt-get install python3.7 -y
RUN apt-get install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools -y
RUN apt-get install python-pip -y
RUN pip install pipenv 
RUN pipenv install
RUN pipenv shell

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app

