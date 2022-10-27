
# ! EXERCÍCIO DO BINGO
from time import sleep


def bingo():
    tempo_rodada = 0.4
    Diego = {'5', '24', '25', '58', '34', '10'}
    Bruna = {'7', '27', '28', '57', '31', '15'}

    gaiolinha = set()

    for numero in range(1, 61):
        gaiolinha.add(str(numero))

    cont = 0
    while True:
        sorteado = gaiolinha.pop()
        print(f'O número sorteado foi: {sorteado}')
        sleep(tempo_rodada)

        cont += 1
        Diego.discard(sorteado)
        Bruna.discard(sorteado)

        if len(Bruna) <= 0:
            print('\nBruna: BINGOOOOO!')
            print(f'Cartela perdedora: {Diego}')
            break
        if len(Diego) <= 0:
            print('\nDiego: BINGOOOOO!')
            print(f'Cartela perdedora: {Bruna}')
            break
    print(f'Quantidade de rodadas: {cont}')


# bingo()

# ! MANIPULAR ARQUIVO DE TEXTO (.txt)
'''
r - read => ler
w - write => escrever / SOBRESCREVE
a - append => adicionar
+ - updade
'''

arquivo = open('Mercadinho', 'a')
arquivo.write('Pao\n')
arquivo.write('Salgadinho\n')
arquivo.write('Sorvete\n')
arquivo.write('Tubaina\n')
# arquivo.close() serve para fechar o arquivo

arquivo = open('Mercadinho', 'r+')
for linha in arquivo:
    # print(linha, end='')
    print(arquivo.readline())

# b GERENCIADOR DE CONTEXTO
with open('Mercadinho', 'a') as arquivo:
    arquivo.write('Pao\n')
    arquivo.write('Salgadinho\n')
    arquivo.write('Sorvete\n')
    arquivo.write('Tubaina\n')

print(arquivo.read())


'''
[1] - ler arquivo
[2] - adicionar no arquivo
[3] - apagar um item
[4] - Ordenar a lista (A-Z)
[5] - deletar o arquivo
[6] - finalizar o programa
'''


def ler():
    pass


while True:
    a = input('o que a pessoa respondeu')
    if a == 1:
        ler()
