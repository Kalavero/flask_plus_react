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

#### GET /pedidos HTTP/1.1

Parametros: nenhum parametro necessário para esse endpoint

Resposta de sucesso (exemplo):

```
HTTP/1.1 200 OK
Content-Type: application/json

"data": [
  {
    "type": "order",
    "id": "1",
    "attributes": {
      "user_id": "42",
      "status": "finished",
      "value": 59.99,
      "currency": 'brl',
      "created_at": "2015-05-22T14:56:29.000Z",
      "updated_at": "2015-05-22T14:56:28.000Z"
    }
  }
]

```
