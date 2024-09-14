# FilmesTop

API da FilmesTop

Documentação da API “Filmes Top”

# Introdução

A API "Filmes Top" permite que os usuários pesquisem filmes por gênero, aluguem filmes, avaliem filmes, vejam detalhes de filmes e visualizem seus aluguéis. 
A API aceita e responde em formato JSON.

# Banco de Dados

Foi utilizado PostgreSQL para criar o banco de dados relacional.

CREATE TABLE IF NOT EXISTS filmestop.usuario(
	usuario_id integer NOT NULL PRIMARY KEY,
	usuario_nome varchar NOT NULL,
	email varchar NOT NULL,
	contato varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS filmestop.filme(
	usuario_id integer NOT NULL PRIMARY KEY,
	usuario_nome varchar NOT NULL,
	email varchar NOT NULL,
	contato varchar NOT NULL
);

CREATE TABLE IF NOT EXISTS filmestop.aluguel(
	usuario_id integer,
	filme_id integer,
	data_locacao date,
	nota integer,
	FOREIGN KEY (usuario_id) REFERENCES filmestop.usuario (usuario_id),
	FOREIGN KEY (filme_id) REFERENCES filmestop.filme (filme_id)
);

INSERT INTO filmestop.filme(filme_id, ano, nome, genero, sinopse, diretor) VALUES
	(1, 1972, 'O Poderoso Chefão', 'Drama', 'Uma família mafiosa luta para estabelecer sua supremacia nos Estados Unidos depois da Segunda Guerra Mundial. Uma tentativa de assassinato deixa o chefão Vito Corleone incapacitado e força os filhos Michael e Sonny a assumir os negócios.', 'Francis Ford Coppola'),
	(2, 2022, 'Exorcismo Sagrado', 'Terror', 'O padre Peter Williams comete um terrível sacrilégio ao ser possuído durante um ritual de exorcismo. Dezoito anos depois, as consequências de seu pecado voltam para assombrá-lo e acabam desencadeando uma batalha ainda maior entre o bem e o mal.', 'Alejandro Hidalgo'),
	(3, 2013, 'Miss Violence', 'Drama', 'Uma menina decide cometer suicídio no dia do seu aniversário de 11 anos. A polícia investiga o caso, mas a família insiste em dizer que foi um acidente, na tentativa de esconder alguma coisa.', 'Alexandros Avranas'),
	(4, 2003, 'A Viagem de Chihiro', 'Fantasia', 'Chihiro e seus pais estão se mudando para uma cidade diferente. A caminho da nova casa, o pai decide pegar um atalho. Eles se deparam com uma mesa repleta de comida, embora ninguém esteja por perto. Chihiro sente o perigo, mas seus pais começam a comer. Quando anoitece, eles se transformam em porcos. Agora, apenas Chihiro pode salvá-los.', 'Hayao Miyazaki');

INSERT INTO filmestop.usuario(usuario_id, nome, email, contato) VALUES
	(1, 'Amanda Ferrer', 'amandinha@email.com', 67890009),
	(2, 'Fernando Noronha', 'noronhabomdemais@email.com', 23440003),
	(3, 'Francisco Silva', 'chicodasilva@email.com', 76890004),
	(4, 'Park Jung Lee', 'annyeonghaseyo@email.com', 33350005);

INSERT INTO filmestop.aluguel(usuario_id, filme_id, data_locacao, nota) VALUES
	(2, 1, '2022 10 23', 8),
	(2, 4, '2022 10 29', 10),
	(3, 2, '2022 09 20', 6),
	(4, 4, '2022 05 01', 10);

# Endpoints

# 1. Homepage

GET /

Descrição: Retorna uma mensagem simples indicando que a API está ativa.

# 2. Pesquisar filmes por gênero 

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


# 3. Alugar um determinado filme 

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

# 4. Atribuir nota a um filme 

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

# 5. Listar informações do filme 

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

# 6. Ver aluguéis

GET / ver_alugueis 

Descrição : Permite que um usuário veja o seu histórico de aluguel.

Resposta:
{
    "nome": "A Viagem de Chihiro",
    "data_locacao": "2023-09-10",
    "nota": 10
}

Essa estrutura cobre as funcionalidades principais da API, facilita o entendimento de como consumir os serviços disponíveis e dá informações sobre o formato de resposta e possíveis erros.
