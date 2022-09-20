import random
from time import sleep
import os

os.system('cls')
# ! comentario
# * comentario
# . comentario
# # comentario
# b comentario

# REVISÃO IF ELIF ELSE
# 7 Faça um script no qual o computador jogue jokenpô com vc

options = 'TESOURA PEDRA PAPEL'
sep_options = options.split(' ')

print('Bora jogar x1 de JOKEPÔ!\n')
player = str.upper(
    input('Digite a sua escolha\n[PEDRA]\n[PAPEL]\n[TESOURA]\n'))
# resp_maiusculo = player.upper()

indice = random.randint(0, 2)
# indice = random.choice(sep_options)

pc = sep_options[indice]

print()
print('='*25)
print()
sleep(1)
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!\n')
sleep(0.5)
print(f'Vc: {player}  PC:{pc}')

if player == 'PEDRA':
    if pc == 'TESOURA':
        print('Vc venceu meu consagrado!!! ¬¬')
    elif pc == 'PAPEL':
        print('HAHA eu venci ps: computador!')
    else:
        print('EMPATE')
elif player == 'PAPEL':
    if pc == 'TESOURA':
        print('HAHA eu venci ps: computador!')
    elif pc == 'PAPEL':
        print('EMPATE')
    else:
        print('Vc venceu meu consagrado!!! ¬¬')
else:
    if pc == 'TESOURA':
        print('EMPATE')
    elif pc == 'PAPEL':
        print('Vc venceu meu consagrado!!! ¬¬')
    else:
        print('HAHA eu venci ps: computador!')

media = 7

if media > 6:
    print('aprovado')
elif media > 4:
    print('recuperação')
else:
    print('reprovado')


# end='' e sep='' do print
print('a', end=', ')
print('b')

print('a', 'b', 'c', sep=' - ')

print('a', 'b', sep=', ', end=' ')
print('é isso')


# ! ESTRUTURAS DE REPETIÇÃO - FOR => para
print('sem FOR')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')

print('com FOR')
palavra = 'melancia'
for vez in range(0, 6):  # para cada vez num intervalo de 0 até 5
    print('oi')

for vez in range(0, 6):  # [0,1 2,3,4,5] só pra fazer um for em algo iteravel
    print(vez)           # iteralvel = varios itens

for letra in palavra:
    print(letra)
# apresenta a ultima coisa que vc guardou na variável
print(letra)

lista = ['eu', 'vc', 'zubumafu']
for item in lista:
    if item == 'zubumafu':
        print('eu conheço essa serie')

for i in range(1, 4):  # [1, 2, 3]
    for j in range(1, 4):  # [1, 2, 3]
        print(f'variável i: {i} variável j: {j}')
    print('terminei o for do j')
print('terminei o for i')


# OPERAÇÕES SIMPLIFICADAS
# SOMA UTILIZANDO O FOR
soma = 0
for i in range(1, 11):  # [0, 1, 2, 3, 4, 5 ... 9]
    soma = soma + i
    # simplifica
    # soma += i
    print(soma)  # incremento

'''
-=  sub = sub - i
/=  div = div / i
*=  mult = mult * i
'''
# somar apenas os números pares
soma_pares = 0
for num in range(1, 11):
    if num % 2 == 0:
        soma_pares += num
print(f'A soma dos números pares deu: {soma_pares}')

soma_pares = 0
for num in range(2, 11, 6):
    soma_pares += num
print(f'A soma dos números pares deu: {soma_pares}')


# EXERCÍCIOS
'''
1) Contagem regressiva de ano novo

2) Apresentar os múltiplos de um número informado pelo usuário entre 0 - 100

3) Refazer o exercício da tabuada

4) Script que solicite 10 números inteiros e que apresente a
soma dos números pares e a soma dos números ímpares

5) Desenvolva um programa que irá pedir 4 números e apresente qual
foi o maior número informado e qual foi o menor
'''
