import json
import os
import random

livros = []
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')


def create():
    global livros
    limpar()
    opcao = input('Deseja adicionar os dados já existentes? s/n\nDigite "n" se quiser uma tabela vazia').lower().strip()
    if opcao == "s":
        pass
    else: 
        livros = []
    tabela = str(input('Dê um nome a tabela que deseja criar: ').lower().strip())
    with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09REBOT\{tabela}.json', 'w', encoding='utf-8') as f:
        json.dump(livros, f, ensure_ascii=False, indent=4)
    
def read():
    tabela = input('Insira o nome do arquivo que deseja consultar: ').strip().lower()
    with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09REBOT\{tabela}.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
        print(f'{'='*45} Livros {'='*45}')
        #ciclo de repetição para gravar todos os nomes na tela
    for livro in dados:
        for chave in livro:
            print(fr'{chave.capitalize()}: {livro.get(chave)}')
        print('='*98)

        #tabela para exibir o proximo nome
        input('Aperte enter para avançar')
        limpar()
        print(98*'=')
            
    #tabela para permitir o avanço do codigo
    limpar()
    input('Aperte enter para sair')
    limpar()

def update():
    global livros
    livro = {}
    limpar()
    tabela = input('Insira o nome da tabela que deseja atualizar: ').strip().lower()
    with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09REBOT\{tabela}.json', 'r', encoding='utf-8') as f:
        dados_livros = json.load(f)
        livros = [dados_livros]

    #coletando os valores a serem atribuidos ao livro
    livro['nome'] = input('Informe o nome do livro: ').strip().title()
    livro['tema'] = input('Informe o gênero do livro: ').strip()
    livro['autor'] = input('Informe o autor do livro: ').strip().title()

    livros.append(livro)

    with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09\{tabela}.json', 'w', encoding='utf-8') as f:
        #variaveis a escrever no arquivo
        json.dump(livros, f, ensure_ascii=False, indent=4)
    # se houver a intenção de criar uma nova tabela com os valores atualizados
    limpar()
    input('Livro cadastrado com sucesso.')


