
# # REVISÃO DA AULA ANTERIOR
from calculos import multiplicar


def fatorial_recursivo(num: int):
    """Função de fatorial com recursividade
    Ex: 5! = 120
    ou seja
    5 x 4 x 3 x 2 x 1 x 0 = 120

    Args:
        num (int): Número que será fatorado

    Returns:
        inteiro: Resultado da conta
    """
    if num < 0:
        print('Não existe fatorail de 0')
    elif num == 0:
        return 1
    else:
        return fatorial_recursivo(num - 1) * num


# print(fatorial_recursivo(5))
# b AGORA COMEÇA O INTERMEDIÁRIO

# ! ARQUIVOS
'''
Criando o arquivo - open() cria um arquivo do tipo .txt
r - read -> ler o arquivo
w - write -> escrever no arquivo
a - append -> adicionar  no arquivo
x - exclusive create -> cria um arquivo

read()
readline()
readlines()
write()
close()
'''

# arquivo = open('teste', 'w+')
# arquivo.write('Diego\n')
# arquivo.write('Pedro\n')
# arquivo.close()

# arquivo = open('teste', 'a+')
# arquivo.write('Victor\n')
# arquivo.write('Camila\n')
# arquivo.write('Vinicius\n')
# arquivo.seek(0)
# print(arquivo.read())
# ! GERENCIADOR DE ARQUIVOS / CONTEXTO => WITH
# personagens = [
#     'Batman',
#     'Super Man',
#     'Mulher Maravilha',
#     'Aquaman',
#     'Flash',
#     'Ajax'
# ]


# with open('teste.txt', 'w+') as arquivo:  # arquivo = open('teste', 'w+')
#     for palavra in personagens:
#         arquivo.write(f'{palavra}\n')
#     arquivo.seek(0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline(), end='')

# ! MÓDULOS / PACOTES
'''
sys => Sistema
random => Tem funções relacionadas a aleatoriedade
os => Tem funções para manipular o sistema operacional
re => expressões regulares
'''

if __name__ == '__main__':
    print(multiplicar(2, 5))
print(__name__)
