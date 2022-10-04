
from time import sleep
from gerenciar_lista import cria_arquivo, adicionar_item, ler_arquivo
from gerenciar_lista import limpa_arquivo, remover_item, excluir_arquivo
from gerenciar_lista import ordenar_arquivo


def menu():
    print('=' * 30)
    print(f'{"App Gerenciador de lista":^30}')
    print('=' * 30)

    resposta = int(input('''
    [1] - Ler Arquivo
    [2] - Escrever no Arquivo
    [3] - Limpar Arquivo
    [4] - Remover Item
    [5] - Ordenar Itens
    [6] - Deletar Arquivo
    [7] - Finalizar
    : '''))
    return resposta


print(f'{"Bem Vinda(o)":^30}\n')
criar_arquivo = str(input('Criar Arquivo [S/N]: ')).upper().strip()[0]
if criar_arquivo == 'S':
    arquivo = input('Insira o nome da lista: ').capitalize().strip()
    usuario = input('Criador da lista: ').capitalize().strip()
    cria_arquivo(arquivo)
    sleep(1)
    while True:
        resposta = menu()
        if resposta == 1:
            ler_arquivo(arquivo, usuario)
            sleep(1.5)
        elif resposta == 2:
            item = input('Qual item deseja adicionar: ').capitalize().strip()
            adicionar_item(arquivo, item)
            sleep(1.5)
        elif resposta == 3:
            limpa_arquivo(arquivo)
            sleep(1.5)
        elif resposta == 4:
            item = input('Qual item deseja remover: ').capitalize().strip()
            remover_item(arquivo, item)
            sleep(1.5)
        elif resposta == 5:
            ordenar_arquivo(arquivo)
            sleep(1.5)
            pass
        elif resposta == 6:
            excluir_arquivo(arquivo)
            sleep(1.5)
            break
        elif resposta == 7:
            print('Fim do programa!')
            break
else:
    print('Então tá né!')
