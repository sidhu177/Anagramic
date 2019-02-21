FROM python:3.7-slim

MAINTAINER "Sid Ramesh"

COPY ./ ./opt/Anagramic

WORKDIR ./opt/Anagramic

RUN pip install --upgrade pip
RUN pip install pipenv 
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000

CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:5000"]

