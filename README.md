
# Documentação da API “Filmes Top”

## Introdução

A API "Filmes Top" permite que os usuários pesquisem filmes por gênero, aluguem filmes, avaliem filmes, vejam detalhes de filmes e visualizem seus aluguéis. 
A API aceita e responde em formato JSON.

## 🗃️ Banco de Dados

Foi utilizado PostgreSQL para criar o banco de dados relacional.

[Tabelas](bancodedados)

## 🤖 Testes

API foi testada no Postman.

[Testes](testes)

## 🎯 Endpoints

### 1. Homepage

### GET > /

_Retorna uma mensagem simples indicando que a API está ativa._


### 2. Pesquisar filmes por gênero 

#### GET > /pesquisar_por_genero

_Retorna uma lista de filmes de determinado gênero._

Exemplo de requisição: 
```
genero = "drama"
```

### 3. Alugar um determinado filme 

#### POST > /alugar 

_Permite que um usuário alugue determinado filme._

BODY (Json) 

Exemplo de requisição:
```
{
  "usuario_id": 2,
  "filme": "Miss Violence"
}
```

### 4. Atribuir nota a um filme 

#### POST > /atribuir_nota

_Permite que um usuário atribua uma nota para o filme que alugou anteriormente._

BODY (Json)

Exemplo de requisição:
```
{
  "usuario_id": 2,
  "filme": "Miss Violence",
  "nota": 10

}
```

### 5. Listar informações do filme 

#### GET > /listar_informacoes

_Permite que um usuário liste as informações daquele filme._

Exemplo de requisição:
```
{
  filme = "A Viagen de Chihiro"
}
```

### 6. Ver aluguéis

#### GET > /ver_alugueis 

_Permite que um usuário veja o seu histórico de aluguel._

Exemplo de requisição:
```
{
  "usuario_id": 4
}
```

#### Essa estrutura cobre as funcionalidades principais da API, facilita o entendimento de como consumir os serviços disponíveis e dá informações sobre o formato de resposta e possíveis erros.
