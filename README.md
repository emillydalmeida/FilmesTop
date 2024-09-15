
# Documentação da API “Filmes Top”

## Introdução

A API "Filmes Top" permite que os usuários pesquisem filmes por gênero, aluguem filmes, avaliem filmes, vejam detalhes de filmes e visualizem seus aluguéis. 
A API aceita e responde em formato JSON.

## 🗃️ Banco de Dados

Foi utilizado PostgreSQL para criar o banco de dados relacional.

## 🤖 Testes

API foi testada no Postman.

## 🎯 Endpoints

### *Homepage

### GET > /

Descrição: Retorna uma mensagem simples indicando que a API está ativa.


### - Pesquisar filmes por gênero 

#### GET > /pesquisar_por_genero

Descrição: Retorna uma lista de filmes de determinado gênero.

Exemplo de requisição: 
```
genero = "drama"
```

### - Alugar um determinado filme 

#### POST > /alugar 

Descrição : Permite que um usuário alugue determinado filme.

BODY (Json) 

Exemplo de requisição:
```
{
  "usuario_id": 2,
  "filme": "Miss Violence"
}
```

### - Atribuir nota a um filme 

#### POST > /atribuir_nota

Descrição : Permite que um usuário atribua uma nota para o filme que alugou anteriormente.

BODY (Json)

Exemplo de requisição:
```
{
  "usuario_id": 2,
  "filme": "Miss Violence",
  "nota": 10

}
```

### - Listar informações do filme 

#### GET > /listar_informacoes

Descrição : Permite que um usuário liste as informações daquele filme.

Exemplo de requisição:
```
{
  filme = "A Viagen de Chihiro"
}
```

### - Ver aluguéis

#### GET > /ver_alugueis 

Descrição : Permite que um usuário veja o seu histórico de aluguel.

Exemplo de requisição:
```
{
  "usuario_id": 4
}
```

#### Essa estrutura cobre as funcionalidades principais da API, facilita o entendimento de como consumir os serviços disponíveis e dá informações sobre o formato de resposta e possíveis erros.
