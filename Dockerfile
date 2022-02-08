FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

WORKDIR = /app/
COPY . .

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install pipenv \ 
    && pipenv install --dev --system --deploy --ignore-pipfile

CMD python src/manage.py migrate --noinput \
    && python src/manage.py runserver 0.0.0.0:8000