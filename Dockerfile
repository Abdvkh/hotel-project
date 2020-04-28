# Dockerfile

FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /hotel

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /hotel/
RUN pipenv install --system

# Copy project
COPY . /hotel/
