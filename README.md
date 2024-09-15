
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

#### GET /

_Retorna uma mensagem simples indicando que a API está ativa._

Saída:
```
Filmes Top
```


### 2. Pesquisar filmes por gênero 

#### GET /pesquisar_por_genero

_Retorna uma lista de filmes de determinado gênero._

Parâmetro: 
```
genero = "drama"
```
Saída:
```
{
  "O Poderoso Chefão"
  "Miss Violence"
}
```


### 3. Alugar um determinado filme 

#### POST /alugar 

_Permite que um usuário alugue determinado filme._

BODY (Json) 

Parâmetro:
```
{
  "usuario_id": 2,
  "filme": "Miss Violence"
}
```
Saída:
```
{
  "message": "Filme alugado com sucesso!"
}
```


### 4. Atribuir nota a um filme 

#### POST /atribuir_nota

_Permite que um usuário atribua uma nota para o filme que alugou anteriormente._

BODY (Json)

Parâmetro:
```
{
  "usuario_id": 2,
  "filme": "Miss Violence",
  "nota": 10

}
```
Saída:
```
{
  "message": "Nota atribuída com sucesso! Nova media para o filme 'filme teste' e 9.0."
}
```

### 5. Listar informações do filme 

#### GET /listar_informacoes

_Permite que um usuário liste as informações daquele filme._

Parâmetro:
```
{
  filme = "A Viagem de Chihiro"
}
```
Saída:
```
{
    "ano": 2003,
    "diretor": "Hayao Miyazaki",
    "filme_id": 4,
    "genero": "Fantasia",
    "nome": "A Viagem de Chihiro",
    "nome_lower": "a viagem de chihiro",
    "nota_final": 9.0,
    "sinopse": "Chihiro e seus pais estão se mudando para uma cidade diferente. A caminho da nova casa, o pai decide pegar um atalho. Eles se deparam com uma mesa repleta de comida, embora ninguém esteja por perto. Chihiro sente o perigo, mas seus pais começam a comer. Quando anoitece, eles se transformam em porcos. Agora, apenas Chihiro pode salvá-los.",
    "total_avaliacoes": 2
}
```

### 6. Ver aluguéis

#### GET /ver_alugueis 

_Permite que um usuário veja o seu histórico de aluguel._

Parâmetro:
```
{
  "usuario_id": 4
}
```
Saída:
```
[
    {
        "data_locacao": "2022-10-23",
        "nome": "O Poderoso Chefão",
        "nota": 8.0
    },
    {
        "data_locacao": "2022-10-29",
        "nome": "A Viagem de Chihiro",
        "nota": 8.0
    },

]
```

#### Essa estrutura cobre as funcionalidades principais da API, facilita o entendimento de como consumir os serviços disponíveis e dá informações sobre o formato de resposta e possíveis erros.
