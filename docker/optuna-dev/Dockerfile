FROM python:3.9.10-buster

RUN pip install -U pip
RUN pip install git+https://github.com/c-bata/optuna.git@dd7ae85749ed532ed24b1b2f4c0c7551fbcf2261
RUN pip install PyMySQL psycopg2-binary cryptography redis pymssql

WORKDIR /work
