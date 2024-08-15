FROM python:3.8-slim

WORKDIR /hacker_news

COPY . /hacker_news

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

