FROM alpine

RUN apk update
RUN apk upgrade
RUN apk add tree git python3 py3-pip
RUN python3 -m pip install --upgrade pip
RUN pip install django
RUN pip install gunicorn
RUN apk add python3-dev mariadb-dev
RUN apk add gcc
RUN apk add libc-dev
RUN pip install mysqlclient
