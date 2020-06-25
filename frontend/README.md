## Frontend

## Requisitos

- docker 19.03.9 ou posterior
- docker-compose version 1.23.2 ou posterior

## Executar

1 - Faça o build do projeto

```shell
docker build . -t react-app
```

2 - Execute o server
```shell
docker run -p 3000:3000 -it react-app

```

3 - o site deve estar disponível em `localhost:3000`

## TODO

- [] Terminar a integração com o backend, disponibilizando o crud de cliente e pedidos.
- [] Criar models para cada serviço para mapear os campos do backend
- [] Adicionar autenticação com o a api
- [] Adicionar login do usuário e sistema de sessão
- [] Adicionar testes unitários
