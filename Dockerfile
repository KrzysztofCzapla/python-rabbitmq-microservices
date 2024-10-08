FROM python:3.11.4-slim-buster

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN pip install --upgrade pip && pip install poetry
RUN poetry install

COPY . .