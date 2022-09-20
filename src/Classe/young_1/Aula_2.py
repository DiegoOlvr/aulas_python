# Manipulação de Strings / texto
'''
imutabilidade = não dá pra mudar depois de crido
\n \t len() split() strip() find() join() replace()
'''
from random import randint
x = 0
x = 5

exemplo = 'Banana maça '
print(exemplo[0])
# \n = pula linha no print
print('\ndie\ngo \nramos')

# \t = identação ou tabulação
print('\tdiego')

# len() = comprimento
print(len(exemplo))

# split() = dividir uma string
n1 = exemplo.split(' ')
print(f'Resultado do split: {n1}')

n2 = exemplo.split()
print('segunda palavra: ' + n2[1])

# strip() = retirar os espaços que tem antes ou depois de uma palavra
fruta = 'banana '
furtaSemEspecos = fruta.strip()
print(f'Essa palavra {furtaSemEspecos} tem {len(furtaSemEspecos)} letras')

exemplo2 = input('Digite uma fruta: ')
print(len(exemplo2))
print(len(exemplo2.strip()))
print(len(exemplo2.rstrip()))  # right
print(len(exemplo2.lstrip()))  # left

# find() = encontrar e devolve a posição
saudacao = 'oi, bom dia, eae'
print(saudacao.find('diego'))

# join() = juntar ou concatenar
frutas = ['banana', 'laranja', 'mamao']
juntada = " e ".join(frutas)
print(juntada)

'''
Eu consigo fazer
um comentário de
multiplas linhas
com 3 aspas simples
'''


# troca de um caracter por outro
# passar a antiga opção e a nova
print(exemplo.replace('a', 'u'))


# ! Operadores de comparação
nome = 'diego'
nome2 = 'Diego'
# igualdade nos usamos dois iguais '=='
print(nome == nome2)

# desigualdade / diferente => !=
print(nome != nome2)

# Maior que
print(nome > nome2)  # ASCII 2

# Menor que
print(nome < nome2)

n1 = 2
n2 = 2
# Maior ou igual
print(n1 >= n2)

# Menor ou igual
print(n1 <= n2)

# Operadores lógicos

# and 'e' em outra linguagem &&
'''
Só saio de casa se (for de dia E não estiver chovendo)
o operador and precisa que as duas opções sejam verdadeiras

if sair and chover:
    'fazer a ação'
'''
# not 'não'
direita = True
esquerda = not direita
print(f'direita: {direita} e esquerda: {esquerda}')
'''
negação ou inversão
'''
# or 'ou'
'''
Só saio de casa se (for de dia OU não estiver chovendo)
o operador or precisa que uma das duas opções sejam verdadeiras
'''
# in 'em'
'''
Se existe o que vc "pergunta" ali dentro
'''
print('Tem a letra K em banana: ')
print('b' in 'banana')


# Condicional simples

'''
SE (a minha condição for verdadeira):
    fará alguma ação
DO CONTRÁRIO:
    fará caso seja falso a condição
'''

if n1 != n2:
    print('Sim, n1 não é igual ao n2')
else:
    print('é vdd, n1 é igual ao n2')

# Condição simplificada
# Passar a ação | fazer a condição | Do contrário
print('Sim, n1 não é igual ao n2') if n1 != n2 else print(
    'é vdd, n1 é igual ao n2')
print('pudim') if n1 != n2 else print('nada haver')

p1 = 6
p2 = 5
media = (p1+p2)/2
if media > 7:
    print('aprovado')
elif media >= 5 and media < 7:
    print('recuperação')
else:
    print('reprovado')


'''
Perguntar (input) duas notas de um aluno
tirar a média dele e informar se
ele foi aprovado ou reprovado
considerando a média 6
'''
n1 = int(input('Digite uma nota: '))
# Condicional composta

'''
Perguntar (input) duas notas de um aluno
tirar a média dele e informar se
ele foi aprovado, recuperação ou reprovado
considerando a média 6
'''

n1 = int(input('Digite uma nota: '))
n2 = int(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media >= 6:
    print('Aprovado')
elif media >= 4:
    print('Recuperação')
elif media >= 2:
    print('Tem que estudar mais')
else:
    print('Reprovado')

# Exercícios
'''
CLÁSSICO
Calcular a média de 3 notas de um aluno qualquer e apresentar se
ele foi aprovado ou não considerando a média 7'''

'''
Fazer um programa que leia um número inteiro e meostre na
tela se ele é PAR ou ÍMPAR
'''


n = int(input('digite um número inteiro: '))
if (n % 2) == 0:
    print("é par poo")
else:
    print("impar")

'''
Escreva um programa que faça o PC "pensar" em um número entre 0 e 5 e
peça para o usuário tentar adivinhar qual foi o número escolhido pelo PC

PC deve retornar se acertou ou não






'''

pc = randint(0, 5)
print('Pensei num número, adivinhe qual é:')
eu = int(input('Acho q é: '))

print('Acertou mizeravi!!!') if eu == pc else print(
    f"ERRRRROU eu pensei no número {pc} e vc disse: {eu}")


'''
Desenvolver um script que me pergunte as horas trabalhadas, o valor da
minha hora cobrada e apresente o meu salário que aumentará 10% se
eu fizer 80h ou menos. Ou 15% quando eu trabalhar acima de 80h
'''
