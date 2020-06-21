FROM python:3.8

ARG FLASK_ENV
RUN mkdir /app

COPY . /app
WORKDIR /app

RUN python3 -m pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "python", "app.py"]
