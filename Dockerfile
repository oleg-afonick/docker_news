FROM python:3.8.10

COPY requirements.txt /temp/requirements.txt
COPY NewsPaper /NewsPaper
WORKDIR /NewsPaper
EXPOSE 8000

RUN python -m pip install --upgrade pip

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password news-user

USER news-user