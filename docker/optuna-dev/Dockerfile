FROM python:3.9.10-buster

RUN pip install -U pip
RUN pip install git+https://github.com/c-bata/optuna.git@04ed7cd6872dcb2c80123880ef98d858f8ee5eb5
RUN pip install PyMySQL psycopg2-binary cryptography redis pymssql

WORKDIR /work
