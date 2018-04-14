FROM python:3.6.5-stretch
RUN mkdir /duckworth
WORKDIR /duckworth
RUN pip install flask sqlalchemy
COPY . /duckworth
