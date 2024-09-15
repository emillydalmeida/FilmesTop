
# Documentação da API “Filmes Top”

## Introdução

A API "Filmes Top" permite que os usuários pesquisem filmes por gênero, aluguem filmes, avaliem filmes, vejam detalhes de filmes e visualizem seus aluguéis. 
A API aceita e responde em formato JSON.

### Banco de Dados

Foi utilizado PostgreSQL para criar o banco de dados relacional.

### Endpoints

#### 1. Homepage

GET /

Descrição: Retorna uma mensagem simples indicando que a API está ativa.

#### 2. Pesquisar filmes por gênero 

GET / pesquisar_por_genero

Descrição: Retorna uma lista de filmes de determinado gênero.

Parâmetros de query:

genero: (obrigatório) O gênero do filme que deseja buscar. Exemplo: acao, comedia, etc.

ERRO 400 
{
  "message": "Por favor, forneca um genero."
}

ERRO 404
{
  "message": "Nao temos filmes desse genero."
}


#### 3. Alugar um determinado filme 

POST/ 

Descrição : Permite que um usuário alugue determinado filme.

BODY (Json) 

usuário_id: (Obrigatório) ID do usuário que está alugando o filme.
filme: (Obrigatório) Filme que o usuário está alugando.

Exemplo de requisição:
{
  ‘usuario_id’: 2,
  ‘filme’: ‘Miss Violence’
}

Resposta:
{
  "message": "Filme alugado com sucesso!"
}

#### 4. Atribuir nota a um filme 

POST/

Descrição : Permite que um usuário atribua uma nota para o filme que alugou anteriormente.

BODY (Json)

usuário_id: (Obrigatório) ID do usuário que está avaliando o filme.
filme: (Obrigatório) Filme que o usuário está avaliando.
nota: (Obrigatório) Nota que o usuário avaliou.

Exemplo :
{
  ‘usuario_id’: 2,
  ‘filme’: ‘Miss Violence’,
  ‘nota’: 10
}

Resposta :
{
  "message": "Nota atribuída com sucesso! Nova media para o filme 'filme teste' e 7.85."
}

#### 5. Listar informações do filme 

GET / listar_informacoes

Descrição : Permite que um usuário liste as informações daquele filme.

Parâmetros de query:

filme: (obrigatório) Nome do filme cujas informações devem ser retornadas.

Resposta:
{
  "filme_id": 1,
  "nome": "O Poderoso Chefão",
  "genero": "Drama",
  "sinopse":"Uma família mafiosa luta para estabelecer sua supremacia nos Estados Unidos depois da Segunda Guerra Mundial. 
  Uma tentativa de assassinato deixa o chefão Vito Corleone incapacitado e força os filhos Michael e Sonny a assumir os negócios.",
  "diretor": "Francis Ford Coppola"
}

#### 6. Ver aluguéis

GET / ver_alugueis 

Descrição : Permite que um usuário veja o seu histórico de aluguel.

Resposta:
{
    "nome": "A Viagem de Chihiro",
    "data_locacao": "2023-09-10",
    "nota": 10
}

Essa estrutura cobre as funcionalidades principais da API, facilita o entendimento de como consumir os serviços disponíveis e dá informações sobre o formato de resposta e possíveis erros.
