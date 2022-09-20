import os

os.system('cls')

# ! condicionais
n1 = 0
n2 = 2

if (n1 > n2):
    print(f'N1 é o maior número: {n1}')
else:
    print(f'N2 é o maior número: {n2}')

# fazer um programa que vai pedir
# duas notas, tirar a media e ver
# se o aluno foi aprovado ou reprovado
# média = 6

n1 = int(input('Digite uma nota: '))
n2 = int(input('Digite uma nota: '))
media = (n1+n2) / 2
print(media)

if media >= 6:    # 6, 7, 8, 9, 10
    print('APROVADO')
elif media > 4:   # 4, 5
    print('RECUPERAÇÃO')
else:             # 1, 2, 3
    print('REPROVADO')

# ! operadores
# # logicos - true or false

''' média = 7
and = e  media > 4 e media < 6 => retorna falso
or = ou  media > 4 ou media < 6 => retorna verdadeiro
not = não negação ou inversão
    direita = true
    not direita = false
in = em ou dentro

palavra = input('Digite uma palavra: ')
if 'a' in palavra:
    print('tem')
else:
    print('não tem')


is = é
direita = true

if direita is true:
    print('sim')
else:
    print('não')
'''

# # comparação
'''
maior >
menor <
maior e igual >=
menor e igual <=
igual  == exemplo: x == 1
diferente !=
um igual significa atribuição
x = 1

'''

# * receber uma velocidade, e vai dizer que a pessoa
# * foi multada ou não
# * qual o limite = 70km/h
