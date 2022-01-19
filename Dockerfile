FROM python:3.9.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /web

RUN apt-get update 

# install dependencies
RUN pip install --upgrade pip

COPY . .

RUN pip install -r requirements.txt