
import os

os.system('cls')
# ! comentario
# * comentario
# . comentario
# # comentario
# b comentario
# meu primeiro comentario
# help(print)

# variaveis, é um espaço da memoria que armazena informação
# nome = (valor que ela recebe)
texto = 'futebol'  # string
numero = 3  # int ou inteiro
decimal = 2.2  # float
boleano = True  # bool

# qual a diferença
lista = ['a', 'g', 'h']
tuplas = ()
a = 11
b = 2
c = a

print(f'o valor de A é: {a}, B: {b} e C: {c}')
print('o valor de A é: '+str(a)+', B: ' + str(b))
print(b)
print(c)

# adição         +
# subtração      -
# divisão        /
# multiplicação  *
# divisão int    //
# resto de divi  %
# potencia       **

print(a + b)
print(a - b)
print(a / b)
print(a * b)
print(a % b)
print(a ** b)
print(a // b)

# COLETAR INFORMAÇÃO DO USUÁRIO
# informacao = input('digite alguma coisa: ')
# print(informacao)

# Fazer um script que vai receber dois números (um depois do outro)
# e no print tem q aparecer a soma deles

# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite outro número: '))

# print(f'A soma do n1: {n1} + n2: {n2} = {n1+n2}')

l1 = 'PROfessor DiEgO'

print(l1.lower())  # minusculo
print(l1.upper())  # maiusculo
print(l1.capitalize())  # só a primeira letra em maiusculo
print(l1.title())  # iniciais em maiusculo
print(len(l1))  # tamanho de uma string

# slice fatiamento
print(l1[:9])
print(l1[10:])
print(l1[::2])
print(l1[-16:2])

print(l1)
