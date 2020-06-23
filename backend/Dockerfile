FROM python:3.8

ENV FLASK_APP=app
ENV FLASK_ENV=development

COPY . /
WORKDIR /

RUN python3 -m pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0"]
