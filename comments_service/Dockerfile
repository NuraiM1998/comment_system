FROM python:3

ENV PYTHONUNBUFFERED 1 

COPY ./requirements.txt /comments_service/requirements.txt

RUN pip install -r requirements.txt
WORKDIR /comments_service

ADD . /comments_service



