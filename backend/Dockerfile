FROM python:3.8

RUN python3 -m pip install pipenv

RUN mkdir /srv/app
WORKDIR /srv/app

ADD Pipfile /srv/app/Pipfile
ADD Pipfile.lock /srv/app/Pipfile.lock

RUN pipenv install --deploy --ignore-pipfile

ADD . /srv/app

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]
