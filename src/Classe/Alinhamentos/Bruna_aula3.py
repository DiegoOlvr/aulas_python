# from random import choice
# from time import sleep

# jogador = input('Digite a sua escolha, pedra, papel ou tesoura: ').lower()
# # indice 0      1       2
# pc = 'pedra papel tesoura'
# pc_escolha = pc.split(' ')

# escolha = choice(pc_escolha)
# sleep(1)
# print('JO...')
# sleep(1)
# print('KEN...')
# sleep(1)
# print('PO...')
# sleep(1)
# print(f'Computador escolheu {escolha}')

# if jogador == 'tesoura':
#     if escolha == 'pedra':
#         print('Jogador perdeu!')
#     elif escolha == 'papel':
#         print('Jogador ganhou!')
#     else:
#         print('empate')
# elif jogador == 'pedra':
#     if escolha == 'pedra':
#         print('empate')
#     elif escolha == 'papel':
#         print('Jogador perdeu!')
#     else:
#         print('Jogador ganhou!')
# else:
#     if escolha == 'pedra':
#         print('Jogador ganhou!')
#     elif escolha == 'papel':
#         print('Empate')
#     else:
#         print('Jogador perdeu!')

# # VARIÁVEIS
# # OPERAÇÕES SIMPLES
# # CONDICIONAIS
# # MANIPULAR STRING

# ! LAÇOS DE REPETIÇÃO
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')
# print('oi')

# b dois tipos de laços
# * FOR = PARA | USAR QUANDO VC SABE QUANTAS VEZES QUER REPETIR
for vez in range(10):  # cria um intervalo de 0 a 9
    print('oi')
print('diego')
# for (variável temporaria) in (intervalo):
# ação identada

nome = 'Bruna Luchtenberg'
for letra in nome:
    print(letra)

for i in range(6, 14):
    print(nome[i])

# * WHILE = enquanto | USAR QUANDO VC Ñ SABE QUANTAS VEZES QUER REPETIR
# cont = 0
# while True:
#     pedir = input('Digite [n] para finalizar: ').lower().strip()[0]
#     if pedir == 'n':
#         break

# while cont < 10:
#     print('Bruna')
#     print('Engraçada')
#     cont = cont + 1  # abreviar para cont += 1

for numero in range(10):  # 0,1,2,3,4,5,6,7,8,9
    if numero == 9:
        break
    elif numero == 6:
        continue
    elif numero == 3:
        pass
    print(numero)
