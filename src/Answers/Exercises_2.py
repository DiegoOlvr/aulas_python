
from datetime import datetime
from operator import itemgetter
from time import sleep
from random import randint


def exercicio_1():
    alunos = dict()

    for n in range(0, 5):
        nome = str(input('Digite o nome da pessoa: ')).strip().capitalize()
        caracteristica = str(
            input(f'Digite uma característica para {nome}: ')
            ).strip().capitalize()
        alunos.update({nome: caracteristica})

    print('')
    for pessoa in alunos:
        print(f'{pessoa} é {alunos[pessoa]}')


def exercicio_2():
    numeros = list()
    sem_repeticoes = list()

    while True:
        n = input('Digite um númerou: [FIM = encerrar] ').upper()

        if n.isnumeric():
            numeros.append(int(n))
        elif n == 'FIM':
            break
        else:
            print('Digite algo válido!!!')

        if n not in sem_repeticoes:
            sem_repeticoes.append(n)

    print(f'Primeira lista: {numeros}')
    print(f'Segunda lista: {sem_repeticoes}')


def exercicio_3():
    ranking = list()
    jogadores = dict()

    for n in range(1, 6):
        player = str(
            input(f'Digite o nome do {n}º jogador: ')).strip().capitalize()
        dice = randint(1, 6)
        print(f'{player} tirou {dice}')

        jogadores.update({player: dice})

    ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
    print('='*20)
    print(f'{"RANKING":^20}')
    print('='*20)
    for i, v in enumerate(ranking):
        print(f'{i+1}º lugar: {v[0]} com {v[1]}')
        sleep(1)


def exercicio_4():
    cadastro = dict()
    valores = list()
    dados = list()
    qtd = 2

    for n in range(0, qtd):
        nome = str(
            input('Digite primeiro nome da pessoa: ')).strip().capitalize()
        ano_nasc = int(input('Digite o ano de nascimento: '))
        hoje = datetime.now().year
        idade = hoje - ano_nasc
        tem_carteira = str(
            input('Possui carteira de trabalho? [S/N] ')).upper().strip()[0]
        valores.append(ano_nasc)
        valores.append(idade)
        valores.append(tem_carteira)

        if tem_carteira == 'S':
            ctps = int(input('Digite o número da sua CTPS: '))
            ano_contratacao = int(
                input('Digite o ano em que foi contratado(a): '))
            salario = int(input('Salário: '))
            valores.append(ctps)
            valores.append(salario)
            valores.append(ano_contratacao)

        dados = valores.copy()
        cadastro.update({nome: dados})
        print('PROOOOXIMO!!!')
        sleep(1)
        valores.clear()
    print(cadastro)
    print('='*20)
    print(f'{"CADASTRADOS":^20}')
    print('='*20)

    for pessoa in cadastro:
        print(f'{pessoa} possui {cadastro[pessoa][1]} anos')
        if cadastro[pessoa][2] == 'S':
            print(f'Sua carteira é: {cadastro[pessoa][3]}')
            print(
                f'''
                Foi contratado em {cadastro[pessoa][5]}
                com um salário de R${cadastro[pessoa][4]:.2f}''')
            aposentar = cadastro[pessoa][1] + \
                (cadastro[pessoa][5] + 35 - datetime.now().year)
            print(f'E irá se aposentar com {aposentar} anos')
        print('')


def exercicio_5():

    pessoas = dict()
    aux = set()
    series = set()
    series_em_comum = set()
    pessoa_em_comum = list()

    qtd_alunos = int(input('Quantas pessoas tem na sua sala: '))

    for aluno in range(qtd_alunos):
        nome = str(
            input(f'\nDigite o nome da {aluno+1}ª pessoa: ')
            ).strip().capitalize()
        qtd_series = int(input(f'De quantas séries {nome} gosta: '))

        for obra in range(qtd_series):
            resp = input(f'Insira o nome da {obra+1}ª obra: ').strip().title()
            aux.add(resp)

        series = aux.copy()
        aux.clear()
        pessoas.update({nome: series})

    print('='*40)
    print(f'{"SÉRIES/ANIMES QUE CADA UM GOSTA":^40}')
    print('='*40)
    for key, value in pessoas.items():
        print(f'{key} gosta de : {value}')

    print('')
    print('='*40)
    print(f'{"SÉRIES/ANIMES EM COMUM":^40}')
    print('='*40)
    for key, value in pessoas.items():
        for chave, valor in pessoas.items():
            if key == chave:
                continue
            else:
                series_em_comum = set(value).intersection(set(valor))
                if series_em_comum:
                    pessoa_em_comum.append(chave)
        if series_em_comum:
            print(
                f'{key} tem {series_em_comum} em comum com {pessoa_em_comum}')
            pessoa_em_comum.clear()
            series_em_comum.clear()


def exercicio_6():
    player_cartela = set()
    pc_cartela = set()
    gaiola = set()
    bingo = False
    tamanho1 = tamanho2 = cont = 0
    for num in range(1, 61):
        gaiola.add(str(num))

    while tamanho1 < 6 and tamanho2 < 6:
        if len(player_cartela) < 7:
            player_cartela.add(str(randint(1, 60)))
            tamanho1 += 1
        if len(pc_cartela) < 7:
            pc_cartela.add(str(randint(1, 60)))
            tamanho2 += 1

    print(f'Sua cartela: {player_cartela}\nCartela do PC: {pc_cartela}')

    while bingo is not True:
        sorteado = gaiola.pop()
        print(f'O número sorteado foi: {sorteado}')
        sleep(0.2)
        cont += 1
        if sorteado in player_cartela:
            player_cartela.remove(sorteado)
            if len(player_cartela) <= 0:
                print('\nPlayer:', end=' ')
                break
        if sorteado in pc_cartela:
            pc_cartela.remove(sorteado)
            if len(pc_cartela) <= 0:
                print('\nPC:', end=' ')
                break
    print('BINGOOOO !!!')


def exercicio_7():
    print('=' * 30)
    print(f'{"GERENCIADOR":^30}')
    print('=' * 30)

    # qtd_jogadores = 0
    pontos = list()
    total = 0
    jogador = {
        'Jogador': '',
        'Pontos': pontos,
        'Total': 0
    }

    # qtd_jogadores = int(input('Quantos jogadores deseja cadastrar: '))

    # for player in range(0, qtd_jogadores):
    jogador['Jogador'] = str(
        input('Digite o nome do jogador: ')).capitalize().strip()
    partidas = int(input('Quantas partidas ele jogou: '))

    for rodada in range(0, partidas):
        num = int(input(f'Quantos pontos ele fez na {rodada+1}ª rodada: '))
        pontos.append(num)
        total += num
        jogador.update({'Total': total})

    for k, v in jogador.items():
        print(f'{k}: {v}')


def exercicio_8():
    alunos = dict()
    menu = prova = -1
    notas = list()
    notas_finais = list()

    while menu != 7:
        nome = str(input('Aluno(a): ')).strip().capitalize()
        if nome == 'Fim':
            break
        for p in range(4):
            while prova < 0 or prova > 10:
                prova = int(input(f'Digite a nota {p+1}º bimestre: '))
            notas.append(prova)
            prova = -1
        notas_finais = notas.copy()
        alunos.update({nome: notas_finais})
        notas.clear()

        print('=' * 30)
        while menu != 6 or menu != 7:

            menu = int(input(
                '''
                \n[1] Menor nota
                \n[2] Maior nota
                \n[3] Média do ano
                \n[4] Todas as notas
                \n[5] Resultado
                \n[6] Próximo aluno(a)
                \n[7] Encerrar\nOPÇÃO:
                '''))

            if menu == 1:
                print(f'A maior nota do {nome} foi: {maior(notas_finais)}')
            elif menu == 2:
                print(f'A menor nota do {nome} foi: {menor(notas_finais)}')
            elif menu == 3:
                print(f'A média anual do {nome} foi: {media(notas_finais)}')
            elif menu == 4:
                print(f'{nome} teve:')
                todasNotas(notas_finais)
            elif menu == 5:
                resul = resultado(notas_finais)
                print(f'{nome} foi: {resul}')
            elif menu == 6:
                break
            elif menu == 7:
                print('FIM DO PROGRAMA - GLÓRIA')
                break


def maior(notas):
    maior = max(notas)

    return maior


def menor(notas):
    menor = min(notas)

    return menor


def media(notas):
    soma = 0
    tamanho_da_lista = len(notas)
    for num in notas:
        soma += num
    media = soma/tamanho_da_lista

    return media


def todasNotas(notas):
    for nota in enumerate(notas):
        print(f'A nota do {nota+1} bimestre foi: {notas[nota]}')


def resultado(notas):
    media_das_notas = media(notas)
    if media_das_notas >= 7:
        resultado = 'APROVADO!'
    elif media_das_notas >= 5:
        resultado = 'RECUPERAÇÃO!'
    else:
        resultado = 'REPROVADO!'

    return resultado
