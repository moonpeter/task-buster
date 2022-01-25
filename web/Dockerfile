FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/web

RUN apt-get update
RUN apt-get install -y gcc musl-dev libffi-dev netcat vim

COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install micropipenv
RUN micropipenv install