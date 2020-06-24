FROM python:3.8

COPY . /srv/app
WORKDIR /srv/app

RUN python3 -m pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]
