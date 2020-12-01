FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /code

ADD . /code

ADD ./requirements /requirements

RUN pip install -r /requirements/base.txt

COPY . /code/
