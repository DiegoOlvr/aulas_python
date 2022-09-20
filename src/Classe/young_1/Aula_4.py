import re as regex
# from time import sleep

# ! comentario
# * comentario
# . comentario
# comentario
# b comentario

# REVISÃO DE FOR
# 2) Apresentar os múltiplos de um número informado pelo usuário entre 0 - 100

mult = int(input("Digite um número: "))

for num in range(0, 101, mult):
    print(f'{num}', end=' ')

'''
4) Script que solicite 10 números inteiros e que apresente a soma
dos números pares e a soma dos números ímpares

5) Desenvolva um programa que irá pedir 4 números e apresente qual foi
o maior número informado e qual foi o menor
'''
print()
soma_par = soma_impar = 0

for vez in range(1, 11):
    num = int(input(f'Digite o {vez}º número: '))
    # na primeira ele fiz que o número é tanto maior e menor
    if vez == 1:
        maior = menor = num
    # do contrário ele faz a verificação
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    # determinar se é par ou impar
    if num % 2 == 0:
        soma_par += num
    else:
        soma_impar += num

print(f'A soma dos pares é: {soma_par} e a soma dos impares: {soma_impar}')
print(f'O menor número é: {menor} e o maior é: {maior}')

# WHILE = enquanto
# precisa de uma condição pra acontecer
print('Exemplos de while')
contador = 10

while contador > 0:
    print(contador)
    # sleep(0.5)
    contador -= 1  # mesma coisa que contador = contador - 1
print('FELIZ ANO NOVO!')

num = 1
while num != 0:
    num = int(input('Digite um número: '))
    if num == 0:
        break  # QUEBRAR O LAÇO
    for n in range(1, 11):
        print(f'{num} X {n} = {num * n}')

    print('FIM DA TABUADA')

print('FIM DO WHILE')

pass  # passa sem fazer nada no cod
# continue para a próxima iteração do seu laço

for num in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    if num == 9:
        break
    if num == 3:
        pass
    if num == 4:
        continue
    print(num)

# condicionais => if elif else
# laço de repetição => for while
# keywords break pass continue


# WHILE COM ELSE =>
print('Exemplo com else')
contador = 10

while contador > 0:
    print(contador)
    # sleep(0.5)
    contador -= 1
else:
    print('fim')


# REGEX = regular expressions
# é uma bibilioteca que já vem com o python - import re
# AS aslias = dar um apelido para alguma coisa

frase = "O python é top demais"
x = regex.search('^O.*demais$', frase)
if x:
    print('sim tem isso ai')
else:
    print('não achei')


'''
PODE DECIDIR QUAL LAÇO UTILIZAR


Faça um programa que receba dez números e usando laços de repetição
calcule e mostre a quantidade de números entre 30 e 90.

Pedir idade e sexo de 5 pessoas e retornar soma e media  de
idade do gênero masculino acima 30 anos e o genero femino entre 18 até 25

'''


# FUNÇÕES DO REGEX
'''
search - devolver um objeto que deu match
findall - devolve uma lista
sub - substituir
split - dividir na onde der match
'''
# METACHARACTERS
# SEQUÊNCIAS ESPECIAIS
# CONJUNTO
