# idade = []
# altura = []

# for item in range(5):
#     idade.append(int(input('Idade: ')))
#     # altura.append(int(input('Altura: ')))

# idade_reverse = idade[-1::-1]
# idade.reverse()
# print(idade)
# print(idade_reverse)


# ! EXERCÍCIO 10
from random import randint
resultados = []
for lance in range(15):
    resultados.append(randint(1, 6))

tamanho_lista = len(resultados)

for numero in range(1, 7):
    contagem = resultados.count(numero)
    porcent = (contagem * 100) / tamanho_lista
    print(f'{numero}: apareceu {contagem} vezes ou {porcent:.2f}%')

# ! EXERCÍCIO 11
perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?", 
    "Já trabalhou com a vítima?"
    ]
respostas = []
for question in perguntas:
    respostas.append(input(question).upper()[0])
