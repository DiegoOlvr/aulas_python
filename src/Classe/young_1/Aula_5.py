import os

os.system('cls')
# ! comentario
# * comentario
# . comentario
# # comentario
# b comentario

# ! REVISÃO DA AULA ANTERIOR
'''
0 - 1 - 1 - 2- 3 - 5 - 8 - 13 - 21
t1-t2
t1 = 0  t1 = 1 
t2 = 1  t2 = 1
t3 = t1+t2

t3 = t1 + t2
'''




# ! OUTROS TIPOS DE DADOS 
# * tipos primitivos = números inteiros, com virgula, boleanos, strings
nome = 'diego'
nome = 'Victor'
print(nome[2])

# # VARIÁVEIS COMPOSTAS
# ! TUPLAS
tupla = (1, 2, 3, 2, 1, 2)
print(type(tupla))
print(tupla[0])
#  índices:  0           1 
tupla2 = ('diego123', 123456, 123456)
print(tupla2)
tupla3 = (1,)
print(type(tupla3))
print(tupla.count(2))
print(tupla.index(2))

for item in tupla:
    print(item)
tuplaConvertida = list(tupla)
print(type(tuplaConvertida))
tuplaConvertida.append(5)

tupla = tuple(tuplaConvertida)
print(tupla)                                

'''
contrutor = tuple()
Imutáveis,
tupla = (1, 2, 3)
permite misturar tipos de objetos diferentes,
indice no 0, ou seja é ordenada
pode ter itens repetidos
tupla = (1, 2, 3)

cuidado ao criar uma tupla com apenas um item
tupla = ('pudim') => não é uma tupla
tupla = ('pudim',) => é uma tupla

acessando
update
unpack (desempacotar)
percorrer
join (juntar)
métodos = count, index
'''
# ! LISTAS
print("\nPARTE FALANDO DA LISTA")
frutas = ['banana', 'maça', 'tomate', 'limão']
for i in range(0,4):
    print(frutas[i])
frutas2 = ['kiwi', 'laranja', 'graviola']

frutas3 = frutas + frutas2
print(frutas3)
frutas.extend(frutas2)
print(frutas)
# como remover um item da lista pop e o remove
print(frutas)
frutas.pop(2)
frutas.remove('banana')
print('lista depois de remover')
print(frutas)
frutas.sort() # ordenar
print(frutas)
frutas.sort(reverse=True) # decrescente
print(frutas)
frutas.append('diego')
print('lista com append')
frutas.insert(2, 'pamonha')
print(frutas)
frutas.clear() # ou del frutas
print(frutas)


'''
contrutor = list()
mútável,
permite misturar tipos de objetos diferentes,
indice no 0, ou seja é ordenada
pode ter itens repetidos
lista = [1, 2, 3]

access, change, add, remove, list comprehension, sort, copy, join
método = append, clear, copy, count, extend, index,
insert, pop, remove, reverse, sort


'''







# ! CONJUNTOS
'''
contrutor = set()
Imutável*,
não ordenado,
indexavel,
não pode ter itens repetidos
conjunto = {1, 2, 3}

access, add, remove, join
método = add, clear, copy, difference, difference_update,
discard, intersection, intersection_update
isdisjoint, issubset, issuperset, pop, remove,
symmetric_difference, symmetric_difference_update, union
update

'''
# ! DICIONÁRIOS
'''
contrutor = dict()
mutável,
ordenado,
indice = chave valor,
não pode ter itens repetidos
conjunto =
{
    "primeiro": 1,
    "segundo": 2,
    "terceiro": 3
}

métodos = clear, copy, fromkeys, get, items, keys, pop,
popitem, setdefault, update, values
'''
