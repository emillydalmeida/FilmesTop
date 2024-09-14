from flask import Flask, request, jsonify
from datetime import datetime
import pandas as pd

# Inicializa o app Flask
app = Flask(__name__)

# Carrega os dados das tabelas
tabela_filmes = pd.read_csv('tabela_filmes.csv')
tabela_usuario = pd.read_csv('tabela_usuario.csv')
tabela_aluguel = pd.read_csv('tabela_aluguel.csv')

# Migração para adicionar as colunas "nota_final" e "total_avaliacoes"
if 'nota_final' not in tabela_filmes.columns:
    tabela_filmes['nota_final'] = 0.0

if 'total_avaliacoes' not in tabela_filmes.columns:
    tabela_filmes['total_avaliacoes'] = 0

#Endpoint da homepage
@app.route('/')
def homepage():
    return 'Filmes Top'

# Endpoint para pesquisar filmes por gênero
@app.route('/pesquisar_por_genero', methods=['GET'])
def pesquisar_por_genero():
    genero = request.args.get('genero')
    #Se o genero for nulo, retorna mensagem de erro
    if genero is None:
        return jsonify({'message': 'Por favor, forneca um genero.'}), 400

    #Converte o genero para letras minusculas
    genero = genero.lower()

    #Converte os generos da tabela para letras minusculas
    filmes = tabela_filmes[tabela_filmes['genero'].str.lower() == genero]

    #Condição para retornar a lista de filmes do determinado gênero
    if not filmes.empty:
        return jsonify(filmes['nome'].tolist())
    else:
        return jsonify({'message': 'Nao temos filmes desse genero.'}), 404

# Endpoint para alugar filme
@app.route('/alugar', methods=['POST'])
def alugar():
    data = request.json
    
    #Se os dados forem nulos, retorna mensagem de erro
    if data is None:
        return jsonify({'message': 'Por favor, forneça o nome do filme.'}), 400

    #Armazena os dados da tabela
    usuario_id = data.get('usuario_id')
    alugar_filme = data.get('filme').lower()

    #Condição para adicionar o novo aluguel na tabela
    if alugar_filme in tabela_filmes['nome'].str.lower().values: 
        filme_id = tabela_filmes.loc[tabela_filmes['nome'].str.lower() ==
        alugar_filme, 'filme_id'].values[0]

        novo_aluguel = {
            'usuario_id': usuario_id,
            'filme_id': filme_id,
            'data_locacao': datetime.now().strftime('%Y-%m-%d'),
            'nota': None
        }

        #Colocando a tabela como global para atualização
        global tabela_aluguel

        #Atualiza a tabela de aluguel
        tabela_aluguel = tabela_aluguel._append(novo_aluguel,
        ignore_index=True)

        #Salva as alterações na tabela
        tabela_aluguel.to_csv('tabela_aluguel.csv', index=False)

        return jsonify({'message': 'Filme alugado com sucesso!'})
    else:
        return jsonify({'message': 'Nao temos esse filme.'}), 404


# Endpoint para atribuir nota
@app.route('/atribuir_nota', methods=['POST'])
def atribuir_nota():
    data = request.json

    #Se o dado não for fornecido recebe uma mensagem de erro
    if data is None:
        return jsonify({'message': 'Por favor, forneça a nota do filme.'}), 400

    #Armazendo usuario, filme e nota em variáveis para manipulação
    usuario_id = data.get('usuario_id')
    filme = data.get('filme').lower()
    nota = float(data.get('nota'))

    #Se a nota for inválida recebe uma mensagem de erro
    if nota < 0 or nota > 10:
        return jsonify({'message': 'A nota deve ser entre 0 e 10.'}), 400

    #Condição para procurar o filme na tabela
    if filme in tabela_filmes['nome'].str.lower().values:
        indice_filme = tabela_filmes['nome'].str.lower().loc[
        tabela_filmes['nome'].str.lower() == filme].index[0]

        #Atualiza o total de avaliações e a nota final
        total_avaliacoes = tabela_filmes.at[indice_filme, 'total_avaliacoes']
        nota_final_atual = tabela_filmes.at[indice_filme, 'nota_final']

        #Calcula a nota final ponderada
        nova_nota_final = (nota_final_atual * total_avaliacoes +
        nota) / (total_avaliacoes + 1)

        #Atualiza a nota final e o total de avaliações
        tabela_filmes.at[indice_filme, 'nota_final'] = nova_nota_final
        tabela_filmes.at[indice_filme, 'total_avaliacoes'] += 1

        #Atualiza o arquivo CSV
        tabela_filmes.to_csv('tabela_filmes_atualizada.csv', index=False)

        #Armazenando o filme id em uma variável para manipulação
        filme_id = tabela_filmes.loc[tabela_filmes['nome'].str.lower()
        == filme, 'filme_id'].values[0]

        if not tabela_aluguel[(tabela_aluguel['usuario_id'] == usuario_id) &
        (tabela_aluguel['filme_id'] == filme_id)].empty:
            indice_aluguel = tabela_aluguel[
            (tabela_aluguel['usuario_id'] == usuario_id)
            & (tabela_aluguel['filme_id'] == filme_id)].index[0]
            tabela_aluguel.at[indice_aluguel, 'nota'] = nota

            #Atualizando a nota na tabela atual
            tabela_aluguel.to_csv('tabela_aluguel.csv', index=False)

        return jsonify({'message':
        f'Nota atribuída com sucesso! Nova media para o filme "{filme}" e {nova_nota_final:.2f}.'
        })
    else:
        return jsonify({'message': 'Voce nao alugou esse filme.'}), 404


# Endpoint para listar informações do filme
@app.route('/listar_informacoes', methods=['GET'])
def listar_informacoes():
    filme = request.args.get('filme')

    if filme is None:
        return jsonify({'message': 'Por favor, forneca o nome do filme.'}), 400

    # Converte o filme para minúsculas
    filme = filme.lower()

    # Converte os nomes dos filmes na tabela para minúsculas e fazer a comparação
    tabela_filmes['nome_lower'] = tabela_filmes['nome'].str.lower()

    if filme in tabela_filmes['nome_lower'].values:
        filme_info = tabela_filmes[tabela_filmes['nome_lower'] ==
                                   filme].iloc[0].to_dict()
        return jsonify(filme_info)
    else:
        return jsonify({'message': 'Nao temos esse filme.'}), 404


# Endpoint para ver alugueis
@app.route('/ver_alugueis', methods=['GET'])
def ver_alugueis():
    usuario_id = request.args.get('usuario_id')

    if usuario_id is None:
        return jsonify({'message': 'Por favor, forneça um ID de usuário.'}), 400

    # Converte usuario_id para o mesmo tipo que está na tabela (int, neste caso)
    try:
        usuario_id = int(usuario_id)
    except ValueError:
        return jsonify({'message': 'ID de usuário inválido.'}), 400

    # Filtra a tabela de aluguel pelos registros do usuário
    alugueis_usuario = tabela_aluguel[tabela_aluguel['usuario_id'] == usuario_id]

    # Verifica se o usuário tem registros de aluguel
    if alugueis_usuario.empty:
        return jsonify({'message': 'Este usuário não possui aluguéis registrados.'}), 404

    # Faz o merge para obter os nomes dos filmes
    alugueis_com_nome_filme = pd.merge(
        alugueis_usuario,
        tabela_filmes[['filme_id', 'nome']],
        how='left',
        on='filme_id'
    )

    # Cria a lista de resposta
    alugueis_lista = []
    for _, row in alugueis_com_nome_filme.iterrows():
        alugueis_lista.append({
            'nome': row['nome'],
            'data_locacao': row['data_locacao'],
            'nota': row['nota']
        })

    return jsonify(alugueis_lista)

# Executa o servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
