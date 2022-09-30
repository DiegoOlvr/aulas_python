
# ! REVISÃO DA AULA ANTERIOR
# '''
# Faça um programa que receba várias idades e que
# calcule e mostre a média das idades digitadas.
# Finalize digitando a idade igual a zero
# '''
# soma_idades = contador = 0
# while True:
#     idades = int(input('Digite a sua idade: '))
#     if idades == 0:
#         break
#     else:
#         soma_idades += idades
#         contador += 1

# media = soma_idades / contador
# print(f'Vc digitou {contador} idades e a média delas é: {int(media)}')

# ! LISTAS
# listas são um conjunto de informações

'''
# # Como criar uma lista vazia
lista_vazia = list()
mercado = []
=================
Listas são indexadas
Ordenadas = organizadas pelo indice
Mutável = vc pode alterar

'''
mercado = ['Chá gelado', 'Chocolate', 'Batata', 'Pão']
mercado2 = ['Coca cola', 'Tapioca', 'Ovo', 'Leite condensado']
print(mercado)
print(mercado[2])
mercado.append('Coca cola')  # ADECIONA SEMPRE AO FIM DA LISTA
print(mercado)
mercado.insert(1, 'Tapioca')  # ADECIONA NO INDICE QUE VC PASSA PRA ELE
print(mercado)
mercado.remove('Tapioca')  # REMOVE O ITEM DA LISTA E SE Ñ HOUVER
print(mercado)             # ELE LEVANTA (RAISE) UM ERRO
mercado.pop()             # REMOVE O ULTIMO ITEM DA LISTA
print(mercado)
print(mercado.index('Batata'))  # RETORNA O PRIMEIRO ÍNDICE ENCONTRADO
mercado.sort(reverse=True)  # ORDENA  A LISTA
print(mercado)
mercado.extend(mercado2)
print(mercado)


# for item in range(4):
#     mercado.append(input('Digite mais um item: ').strip().capitalize())


for numero, coisa in enumerate(mercado):
    print(f'O {numero+1}º item é: {coisa}')

# ! TUPLAS
'''
É tipo listas, porém eu não posso mudar (alterar)
imutáveis
tuplinha = tuple()
'''
tuplinha = ('Sorvete', 1, 'Café', 33, 'Sorvete')
print(tuplinha.count('Sorvete'))
print(tuplinha.index('Sorvete'))
aux = list(tuplinha)
print(tuplinha)
print(aux.pop())

# ! SET e DICT
'''
Set = conjuntos
Guardar várias informações que vc não deseja que sejam repetidas
Não aceita duplicatas
Não são ordenados (pra texto)
E posso criar assim:
conjuntinho = set()

Dict
key: value
chave: valor
Bruna: ['Engraçada', 'Adolescente', 'Divertida']
'''
conjuntinho = {'Bruna', 'Leonardo', 'Fabiana', 'Calvin'}
conjuntinho2 = {'Bruna', 'Camila', 'Victor', 'Vinicius', 'Pedro'}
conjuntinho.update(conjuntinho2)
print(conjuntinho)
conjuntinho_numeros = {2, 1, 17, 33, 28}
print(conjuntinho_numeros)
