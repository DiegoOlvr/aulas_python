def criar(nome: str, criador: str):
    arquivo = open(f'{nome}.txt', 'w')
    arquivo.write(f'{nome} - Criada por {criador}\n')


def ler(file: str):
    with open(f'{file}.txt', 'r') as arquivo:
        arquivo.seek(0)
        print(arquivo.read())


def escrever(file: str):
    with open(f'{file}.txt', 'a') as arquivo:
        print('escreva suas compras (enter/0 para finalizar): ')
        while True:
            texto = input('')
            if texto == '' or texto == '0':
                break
            arquivo.write(texto + '\n')


def limpar(arquivo: str):
    open(f'{arquivo}.txt', 'w').close()


def limparlinha(file: str, plinha: int):
    with open(f'{file}.txt', 'r+') as arquivo:
        linhas = arquivo.readlines()
        pos = 1
        arquivo.seek(0)
        open(f'{file}.txt', 'w').close()
        for linha in linhas:
            if pos != plinha:
                arquivo.write(linha)
            pos += 1


def ordem_alfabetica(arquivo: str):
    with open(f'{arquivo}.txt', 'r+') as file:
        titulo = file.readline()
        linhas = file.readlines()
        linhas.sort()
        file.seek(0)
        file.write(titulo)
        file.writelines(linhas)


def deletar(arquivo: str):
    import os
    os.remove(f'{arquivo}.txt')


def finalizar(arquivo):
    file = open(f'{arquivo}.txt', 'r')
    file.close()
