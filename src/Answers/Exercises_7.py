
from itertools import permutations
from random import randint, sample


def exercicio_1(n):
    for i in range(n):
        i += 1
        print(f'{str(i) * i} ')
# # EXERCICIO 2


def imprimeLinha(numero: int):
    for n in range(1, numero + 1):
        print(f'  {n} ', end='')
    print()


def imprimeSequencia(numero: int):
    for numero in range(numero + 1):
        imprimeLinha(numero)


def exercicio3(a, b, c):
    return a + b + c


def exercicio4(x):
    if x <= 0:
        return "N"
    elif x > 0:
        return "P"


def exercicio5(taxaimposto, custo):
    return (0.01 * taxaimposto) * custo + custo


def hora(h, m):
    b = h / 12
    if b <= 1:
        hh = str(h)
        print('Sua hora: ' + hh + ':', end='')
    elif b > 1 and b < 2:
        hhh = str(h - 12)
        print('Sua hora: ' + hhh + ':', end='')
    else:
        print('Formato de hora invalido')
    if b <= 1 and m <= 60:
        print(m, 'a.m')
    elif b > 1 and m <= 60:
        print(m, 'p.m')
    else:
        print('Formato de minutos invalidos')


while True:
    print('digite 666 para sair')
    h = int(input('Informe a hora:'))
    if h == 666:
        break
    m = int(input('Informe os minutos: '))
    hora(h, m)

qtPrest = []
listaVc = []
ct = 0


def funcVP(VP, NumDias):
    Vpm = VP * 1.03
    valorC = round(Vpm * ((1 + 0.001) ** NumDias), 2)
    listaVc.append(valorC)
    print('Valor corrigido:', valorC)
    global ct
    ct += 1
    qtPrest.append(ct)


while True:
    VP = float(input('Digitr o valor da prestação: (0 para sair) '))
    if VP == 0:
        break
    NumDias = int(input('Quantos dias que está em atraso: '))
    funcVP(VP, NumDias)
print('Quantidade de prestações pagas: ', ct)
print('Valor total de prestações pagas no dia: R$', round(sum(listaVc)), 2)


def exercicio8(n):
    s = str(n)
    return len(s)


def exercicio_9(n):
    inverte = str(n)
    print(inverte[::-1])


def craps():
    # Função para jogar os dados
    def jogar():
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
        print(
            f'DADO AMARELO {dado1} e DADO AZUL {dado2} e SOMA {dado2 + dado1}')
        return dado1 + dado2

    cont = ganho = perda = 0
    while True:
        a = input('jogar: ')
        if a in "nN":
            break
        valor = jogar()

        if cont == 0 and valor == 7 or valor == 11:
            print('come-out roll GANHOOOOUUU')
            ganho += 1
            cont = 0
        elif cont == 0 and valor == 2 or valor == 3 or valor == 12:
            print('come-out roll PERDEEEEUUUU')
            cont = 0
            perda += 1
        elif cont == 0:
            passLine = valor
            cont = 1
            print('jogue mais uma vez')
            continue
        elif cont == 1:
            if passLine == valor:
                print('Pass line  GANHOOOOUUU')
                ganho += 1

            else:
                print('PERDEEEEUUUU \nTenta novamente')
                perda += 1
            cont = passLine = 0
        print('-*' * 15)
    print('OBRIGADO POR SE DIVERTIR COM CRAPS EM NOSSO CASSINO')
    print(f'você ganhou {ganho} e perdeu {perda}')


def dataExtenso(data):
    meses = [
        (),
        ['janeiro', 31],
        ['fevereiro', 29],
        ['março', 31],
        ['abril', 30],
        ['maio', 31],
        ['junho', 30],
        ['julho', 31],
        ['agosto', 31],
        ['setembro', 30],
        ['outubro', 31],
        ['novembro', 30],
        ['dezembro', 31]
    ]

    data = data.split('/')
    dia, mes, ano = int(data[0]), int(data[1]), int(data[2])
    if mes == 2:
        meses[mes][1] = anoBissexto(ano)
    if 0 < mes < 13 and 0 < dia <= meses[mes][1]:
        print(f'{dia} de {meses[mes][0]} de {ano}')
    else:
        print('NULL')


def anoBissexto(ano):  # verifica se ano é bissexto
    if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
        return 29
    else:
        return 28


def exercicio_12(s):
    embaralha = sample(s, len(s))  # String vira lista
    a = ''.join(embaralha)  # lista vira string
    print(a)


def primeria_linha_coluna(linha, coluna):
    contC = 0
    contL = 0
    c = ''
    l1 = ''
    while (contL < linha) and (contC < coluna):
        if contL == 0:
            l1 = '+'
            for i in range(coluna):
                c += '-'
            l1 = '+'
        contL += 1
        contC += 1
    print(l1+c+l1)


def outras_linhas(linha, coluna):
    contC = 0
    contL = 0
    c = ''
    l2 = ''
    while contL < linha:
        if contL == 0:
            l2 = '|'
            for i in range(linha):
                c += ' '
            l2 = '|'
        contL += 1
        contC += 1
        print(l2+c+l2)


def ultima_linha(linha, coluna):
    contL = 0
    contC = 0
    l3 = ''
    c = ''
    while (contL < linha) and (contC < coluna):
        if contL == 0:
            l3 = '+'
            for i in range(coluna):
                c += '-'
            l3 = '+'
        contL += 1
        contC += 1
    print(l3+c+l3)


linha = int(input('Informe o número de linhas: '))
coluna = int(input('Informe o número de colunas: '))

primeria_linha_coluna(linha, coluna)
outras_linhas(linha, coluna)
ultima_linha(linha, coluna)


def validaTabela(tabela):  # Verifica se a tabela é válida
    if sum(tabela[:3]) == sum(tabela[3:6]) == sum(tabela[6:10]):
        if sum(tabela[::3]) == sum(tabela[1::3]) == sum(tabela[2::3]):
            if sum(tabela[::4]) == sum(tabela[2:8:2]):
                print(tabela, ' valida ')
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0


def gera(tab):  # gerar as matrizes possíveis
    cont = 0
    validos = 0
    for i in permutations(tab, 9):
        cont += 1
        validos += validaTabela(i)
    print(f'total de verificações {cont} e matriz válidas {validos}')


tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
