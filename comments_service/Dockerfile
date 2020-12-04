FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /comments_service

ADD . /comments_service

COPY ./requirements.txt /comments_service/requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]

