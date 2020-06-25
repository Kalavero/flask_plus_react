## Sistema de pedidos

## Requisitos

- docker 19.03.9 ou posterior
- docker-compose version 1.23.2 ou posterior

## Executar

1 - Faça o build do projeto

```shell
docker-compose build
```

2 - Rode o seguinte comando para criar o banco:

```shell
docker-compose run --rm db bash

su - postgres

psql -h db -U app # coloque o password: 'password' conforme definido no docker-compose)

CREATE DATABASE app_db;

\q
```

3 - Saia do container e rode:

```shell
docker-compose up
```

### Enpoints

#### GET /users HTTP/1.1

Parametros: nenhum parametro necessário para esse endpoint

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": "42",
    "first_name": "andre",
    "last_name": "souza",
    "email": 'lukkalavero@yahoo.com',
  }
]

```

#### GET /users/<id> HTTP/1.1

Parametros: id(obrigatório)

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "42",
  "first_name": "andre",
  "last_name": "souza",
  "email": 'lukkalavero@yahoo.com',
}

```

#### POST /users HTTP/1.1

Parametros: first_name, last_name, email (todos os parametros são obrigatórios)

Resposta de sucesso (exemplo):

```
HTTP/1.1 201 CREATED
Content-Type: application/json

{
  "id": "42",
  "first_name": "andre",
  "last_name": "souza",
  "email": 'lukkalavero@yahoo.com',
}

```

#### PUT /users/<id> HTTP/1.1

Parametros: id(obrigatório), first_name, last_name, email

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "42",
  "first_name": "andre",
  "last_name": "souza",
  "email": 'lukkalavero@yahoo.com',
}

```

#### DELETE /users/<id> HTTP/1.1
Parametros: id(obrigatório)

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "42",
  "first_name": "andre",
  "last_name": "souza",
  "email": 'lukkalavero@yahoo.com',
}

```

