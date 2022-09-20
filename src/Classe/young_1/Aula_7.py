
# ! REVOLVENDO A LISTA DA AULA ANTERIOR
from operator import itemgetter
from random import randint
from time import  sleep


def exercicio1():
    pessoas = dict()

    for n in range(0, 4):
        nome = input(f'Digite o nome da {n+1}ª pessoa: ').strip().capitalize()
        caracteristica = input(f'Digite uma característica do(a) {nome}: ')
        pessoas.update({nome: caracteristica})

    print('')
    for aluno in pessoas:
        print(f'{aluno} é {pessoas[aluno]}')

def exercicio2():
    numeros = list()
    sem_repeticoes = list()
    conjunto = set()
    while True:
        n = input(f'Digite um número: [FIM = encerramento] ').upper()
        
        if n.isnumeric():
            numeros.append(n)
        elif n == 'FIM':
            break
        else:
            print('Digite algo válido!!!')
        conjunto.update(n)
        if n not in sem_repeticoes:
            sem_repeticoes.append(n)
        
    print(f'Primeira lista: {numeros}')
    print(f'Segunda lista: {sem_repeticoes}')
    print(f'O conjunto: {conjunto}')

def exercicio3():
    jogadores = dict()
    ranking = list()

    for n in range(1, 6):
        player = input(f'Digite o nome do {n}º jogador: ').strip().capitalize()
        dice = randint(1, 6)
        print(f'{player} tirou {dice}')
        jogadores.update({player: dice})
    # [[nome, valor], [nome, valor], [nome, valor], [nome, valor], [nome, valor], ]
    ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
    print('='*20)
    print(f'{"RANKING":^20}')
    print('='*20)
    for i, v in enumerate(ranking):
        print(f'{i+1}º lugar: {v[0]} com {v[1]}')
        sleep(1)

def exercicio6():
    gaiola = set()
    player_cartela = set()
    pc_cartela = set()
    tamanho1 = tamanho2 = cont = 1

    while tamanho1 <= 6 and tamanho2 <= 6:
        if len(player_cartela) < 7:
            player_cartela.add(str(randint(1, 60)))
            tamanho1 += 1
        if len(pc_cartela) < 7:
            pc_cartela.add(str(randint(1, 60)))
            tamanho2 += 1
    print(f'Sua cartela: {player_cartela}\nCartela do PC: {pc_cartela}')
    for num in range(1, 61):
        gaiola.add(str(num))
    
    while True:
        sortear = gaiola.pop()
        print(f'O número sorteado foi: {sortear}')
        sleep(0.1)
        cont += 1
        if sortear in player_cartela:
            player_cartela.remove(sortear)
            print(f'\nPlayer: aeeee')
            tamanho1 -= 1
            print(tamanho1)
            if tamanho1 == 1:
                print(f'Cartela perdedora{pc_cartela}')
                print(f'\nPlayer: ', end=' ')
                break
        
        pc_cartela.discard(sortear)
        if len(pc_cartela) <= 0:
            print(f'Cartela perdedora{player_cartela}')
            print(f'\nPC: ', end=' ')
            break
            
    print('BINGOOOOOO!!!')
    print(f'Tivemos {cont} rodadas')
    



# ! FUNÇÕES
'''
Um conjunto de algoritmos que serão executados
print() => mostra algo no terminal ou output (saida)
len()
max(), min(), strip(), 
função é como se fosse uma variável
ela armazena comandos

toda vez que formos usar uma função, precisa por os parenteses
nome_da_função()

para criar as nossas funções 
def = definir, nome da função, () e dentro deles pode ter algo ou não
def nome_da_função(parametros*):

'''