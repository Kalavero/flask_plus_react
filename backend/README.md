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

#### GET /clientes HTTP/1.1

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

#### GET /clientes/<id> HTTP/1.1

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

#### POST /clientes HTTP/1.1

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

#### PUT /clientes/<id> HTTP/1.1

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

#### DELETE /clientes/<id> HTTP/1.1
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

#### GET /pedidos HTTP/1.1

Parametros: nenhum parametro necessário para esse endpoint

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": "42",
    "status": "pending",
    "created_at": "2020-06-25T02:46:25.610466",
    "value": '25.9',
    "user_id": '1',
  }
]

```

#### GET /pedidos/<id> HTTP/1.1

Parametros: id(obrigatório)

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "42",
  "status": "pending",
  "created_at": "2020-06-25T02:46:25.610466",
  "value": '25.9',
  "user_id": '1',
}

```

#### POST /pedidos HTTP/1.1

Parametros: user_id, value (todos os parametros são obrigatórios)

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

#### PUT /pedidos/<id> HTTP/1.1

Parametros: id(obrigatório), value, status, user_id, created_at

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": "42",
  "status": "pending",
  "created_at": "2020-06-25T02:46:25.610466",
  "value": '25.9',
  "user_id": '1',
}

```

#### DELETE /pedidos/<id> HTTP/1.1
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

## TODO

- [] Adicionar tratamento de erros
- [] Adicionar autenticação via token
- [] Garantir que a API sempre retornará um json
- [] Alterar update para permitir apenas parametros específicos
