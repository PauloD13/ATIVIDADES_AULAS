import json
import os
import random
#imports

#definindo variaveis e funções globais
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
nome = None
livros = []

#função de abertura do codigo
def saudacao():
    limpar()
    #chamando variavel global
    global nome
    input('Olá usuario, seja bem vindo! ')
    nome = input('Qual o seu nome?\n').title()

    #testando variavel
    input(f'Seja bem vindo {nome}!')
    return nome

def menu():
    #função de menu
    limpar()
    print(20*'=','MENU DE OPÇÕES',20*'=')
    print('1 - Criar uma nova tabela')
    print('2 - Consultar uma tabela')
    print('3 - Adicionar em uma tabela')
    print('4 - Deletar uma tabela')
    print('5 - Sair do sistema')
    print(57*'=')

    #definindo uma interação com coleta de uma variavel
    opcao = int(input('Digite a opcao desejada: '))
    #return com o valor da variavel
    return opcao


def create():
    limpar()
    #criando o arquivo json
    global livros
    #interação coletando valor de s ou n
    opcao = str(input('Deseja cadastrar os dados já existentes? s/n ').strip().lower())

    #em caso de n os valores da lista deverão ser resetados
    if opcao == "n":
        livros = []
    else:
        pass
    
    #criando e nomeando o novo arquivo .json onde serão amramazenados valores
    novo_arquivo = input('Informe o nome do arquivo: ').strip().lower()
    with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09\{novo_arquivo}.json', 'w', encoding='utf-8') as f:
        #variaveis a escrever no arquivo
        json.dump(livros, f, ensure_ascii=False, indent=4)
    limpar()
    print('Arquivo salvo com sucesso!')

    
def read():
    limpar()
    #chamando variaveis da função
    livro = {}
    global livros
    #solicitando leitura do arquivo
    tabela = input('Digite o nome do arquivo: ').strip().lower()

    #abrindo o arquivo
    with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09\{tabela}.json', 'r', encoding='utf-8') as f:
        dados = json.load(f)
        #carregando os dados e exibindo na tela
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
    limpar()
    #chamando variaveis da função
    livro = {}
    global livros

    #coletando os valores a serem atribuidos ao livro
    livro['nome'] = input('Informe o nome do livro: ').strip().title()
    livro['tema'] = input('Informe o gênero do livro: ').strip()
    livro['autor'] = input('Informe o autor do livro: ').strip().title()

    livros.append(livro)
            
    #salvando os dados e finalizando o caso
    opcao = input('Deseja registrar numa tabela existente? s/n\nLembrando que esta ação sobrescreverá dados já existentes\n').lower().strip()
    if opcao == "s":
        tabela = str(input('Em qual tabela desejas cadastrar? ').strip().lower())
        with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09\{tabela}.json', 'w', encoding='utf-8') as f:
            #variaveis a escrever no arquivo
            json.dump(livros, f, ensure_ascii=False, indent=4)
    # se houver a intenção de criar uma nova tabela com os valores atualizados
    else:
        print('Para adicionar a uma nova tabela selecione a opção criar tabela no menu.')
    limpar()
    print('Livro cadastrado com sucesso.')

def delete():
    #chamando as variaveis da função
    global livros
    opcao = input('1 - Limpar dados recém-cadastrados\n2 - Apagar uma tabela existente\n').strip()

    #escolha de caso, se for do interesse do usuario limpar a memoria e limpar as listas
    if opcao == "1":
        livros = []
    #se for do interesse do usuarios limpar todos os valores da tabela escolhida
    elif opcao == "2":
        tabela = str(input('Informe o nome do arquivo: ').strip().lower())
        apagar = []
        with open(fr'C:\Users\ead\Documents\ATIVIDADES_AULAS\AULA_09\{tabela}.json', 'w', encoding='utf-8') as f:
            #variaveis a escrever no arquivo
            json.dump(apagar, f, ensure_ascii=False, indent=4)
    #em caso de erro o esle executa um print
    else:
        print('opção invalida.')
        print('Retornando para o menu.')
