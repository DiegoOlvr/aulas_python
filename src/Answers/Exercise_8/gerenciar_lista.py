from datetime import date
import os


def cria_arquivo(nome_do_arquivo: str):
    """Função para criar um arquivo txt com título de quem
    criou e a data que foi criada

    Args:
        nome_do_arquivo (str): Nome do arquivo
    """
    with open(nome_do_arquivo, 'w+'):
        pass
    print('Arquivo criado com sucesso!\n')


def adicionar_item(nome_do_arquivo: str, item: str):
    """Função para adicionar novos itens a lista sem excluir
    os anteriores

    Args:
        nome_do_arquivo (str): Nome do arquivo
        item (str): Nome do item que será adicionado
    """
    with open(nome_do_arquivo, 'a+') as arquivo:
        arquivo.write(item + '\n')
    print(f'{item} foi adicionada a lista!\n')


def ler_arquivo(nome_do_arquivo: str, criador: str):
    """Função que irá apresentar no terminal
    o conteúdo do arquivo solicitado

    Args:
        nome_do_arquivo (str): Arquivo que deseja ver
        criador (str): Quem criou o arquivo
    """
    cabecalho(criador)
    with open(nome_do_arquivo, 'r') as arquivo:
        for conteudo in arquivo:
            print(conteudo, end='')


def limpa_arquivo(nome_do_arquivo: str):
    """Função para remover todos os itens contidos na lista

    Args:
        nome_do_arquivo (str): Remove tudo da lista deixando apenas o cabeçalho
    """
    with open(nome_do_arquivo, 'w+') as arquivo:
        arquivo.write('')


def remover_item(nome_do_arquivo: str, item: str):
    """Função que irá remover um item selecionado pelo usuário
    da lista do arquivo

    Args:
        nome_do_arquivo (str): Nome do arquivo
        item (str): Qual item será excluido
    """
    itens_do_arquivo: list = []
    item += '\n'
    with open(nome_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            itens_do_arquivo.append(linha)
        print('itens do arquivo', itens_do_arquivo)
        if item in itens_do_arquivo:
            itens_do_arquivo.remove(item)
            print(f'{item}', end='')
            print('foi removido com sucesso!')
            with open(nome_do_arquivo, 'w+') as file:
                for linha in itens_do_arquivo:
                    file.write(f'{linha}\n')
        else:
            print('Não há esse item na lista!')


def cabecalho(criador: str):
    """Função para apresentar um título

    Args:
        criador (str): Nome do usuário quem criou a lista
    """
    data_atual = date.today()
    print('=' * 30)
    print(f'lista do {criador}\n')
    print(f'Criada em: {data_atual}')
    print('=' * 30)
    print('Itens:\n')


def excluir_arquivo(nome_do_arquivo: str):
    """Função para excluir o arquivo

    Args:
        nome_do_arquivo (str): Nome do arquivo
    """
    os.remove(nome_do_arquivo)
    print(f'O arquivo {nome_do_arquivo} foi excluido!')


def ordenar_arquivo(nome_do_arquivo: str):
    """Função que ordena o arquivo em ordem alfabética

    Args:
        nome_do_arquivo (str): Nome do arquivo
    """
    item_ordenados: list = []
    with open(nome_do_arquivo, 'r+') as arquivo:
        for linha in arquivo:
            item_ordenados.append(linha)
        item_ordenados.sort()
        with open(nome_do_arquivo, 'w+') as arquivo:
            for linha in item_ordenados:
                arquivo.write(f'{linha}\n')
    print('Sua lista foi ordenada alfabéticamente!')
