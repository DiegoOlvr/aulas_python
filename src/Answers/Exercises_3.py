'''
1) Contagem regressiva de ano novo

2) Apresentar os múltiplos de um número informado pelo usuário entre 0 - 100

3) Refazer o exercício da tabuada

4) Script que solicite 10 números inteiros e que
apresente a soma dos números pares e a soma dos números ímpares

5) Desenvolva um programa que irá pedir 4 números e apresente
qual foi o maior número informado e qual foi o menor
'''
# EXERCÍCIO 1
from time import sleep

print('CONTAGEM REGRESSIVA')
print('='*25)
print()

for num in range(10, 0, -1):
    print(num)
    sleep(1)

print('FELIZ ANO NOVO')

for i in range(0, 50):
    print()

# EXERCÍCIO 2
print('MULTIPLOS ENTRE 0 A 100')
print('='*25)
print()

mult = int(input('Digite o multiplo que deseja conhecer: '))
print(f"Os Multiplos de {mult} são: ")
for result in range(0, 100, mult):
    print(f'{result}', end=" ")

for i in range(0, 50):
    print()

# EXERCÍCIO 3
print('TABUADA MELHORADA')
print('='*25)
print()

num = int(input('Digite o valor que deseja saber a tabuada: '))

for item in range(0, 11):
    print(f'{num} X {item} = {num*item}')

for i in range(0, 50):
    print()


# EXERCÍCIO 4
print('SOMA DE PARES E ÍMPARES')
print('='*25)
print()

soma_pares = soma_impares = 0

for vez in range(0, 10):
    num = int(input(f'Digite o {vez+1}º número: '))
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num
print(f'A soma dos PARES foi: {soma_pares} e dos ÍMPARES foi: {soma_impares}')

for i in range(0, 50):
    print()


# EXERCÍCIO 5
print('MAIOR E MENOR')
print('='*25)
print()

maior = 0
menor = 9999999999  # gambiarra

for vez in range(0, 4):
    num = int(input(f'Digite o {vez+1}º número: '))
    if vez == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'O MAIOR número foi: {maior} e o MENOR foi: {menor}')
