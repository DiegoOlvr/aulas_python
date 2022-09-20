
# # Exercício 1
def exercicio_1():
    print('=' * 30)
    print(f'{"Exercício 1":^30}')
    print('=' * 30)

    lista_de_numeros = list()
    for num in range(1, 3):
        valores = int(input(f'Digite o {num}º número: '))
        lista_de_numeros.append(valores)
    print(lista_de_numeros)

# # Exercício 2
def exercicio_2():
    print('=' * 30)
    print(f'{"Exercício 2":^30}')
    print('=' * 30)

    numeros = list()
    for num in range(1, 11):
        valor = int(input(f'Digite o {num}º número: '))
        numeros.append(valor)
    # ou numeros.reverse()
    for n in range(len(numeros), 0, -1):
        print(numeros[n-1])

# # Exercício 3
def exercicio_3():
    print('=' * 30)
    print(f'{"Exercício 3":^30}')
    print('=' * 30)

    notas = list()
    for i in range(1, 5):
        notas.append(int(input('Digite uma nota: ')))

    media = sum(notas)/len(notas)
    print(f'As notas fora: {notas} e a sua média: {media}')

# # Exercício 4
def exercicio_4():
    print('=' * 30)
    print(f'{"Exercício 4":^30}')
    print('=' * 30)

    consoantes = list()
    tem_vogal = 0

    for vez in range(1, 11):
        letra = str(input('Digite uma letra: ')).lower().strip()[0]
        if letra not in 'aeiou':
            consoantes.append(letra)
    print(f'identifiquei {len(consoantes)} consoantes: {consoantes}')

# # Exercício 5
def exercicio_5():
    print('=' * 30)
    print(f'{"Exercício 5":^30}')
    print('=' * 30)

    pares = list()
    impares = list()
    todos = list()

    for num in range(1, 6):
        todos.append(int(input('Digite um número: ')))
        if todos[num] % 2 == 0:
            pares.append(todos[num])
        else:
            impares.append(todos[num])

    print(f'As listas com todos os números: {todos}')
    print(f'A lista com números pares: {pares}')
    print(f'A lista com números impares: {impares}')

# # Exercício 6
def exercicio_6():
    print('=' * 30)
    print(f'{"Exercício 6":^30}')
    print('=' * 30)

    lista6 = list()
    mult = 1

    for num in range(1, 6):
        lista6.append(int(input('Digite um número: ')))
        mult *= lista6[num]
    print(f'Os números digitados foram: {lista6}, sua soma é: {sum(lista6)} e a multiplicação: {mult}')

# # Exercício 7
def exercicio_7():
    print('=' * 30)
    print(f'{"Exercício 7":^30}')
    print('=' * 30)

    idade = list()
    altura = list()

    for vez in range(1, 3):
        idade.append(int(input(f'Digite a idade da {vez}ª pessoa: ')))
        altura.append(float(input(f'Digite a altura da {vez}ª pessoa: ')))

    for pessoa in range(len(idade)-1, -1, -1):
        print(f'A {pessoa+1}ª possui {idade[pessoa]} anos e {altura[pessoa]:.2f} de altura')

# # Exercício 8
def exercicio_8():
    print('=' * 30)
    print(f'{"Exercício 8":^30}')
    print('=' * 30)

    lista1 = list()
    lista2 = list()
    lista3 = list()

    for item in range(0, 10):
        lista1.append(int(input(f'Digite o {item+1}º número da lista1: ')))

    for item in range(0, 10):
        lista2.append(int(input(f'Digite o {item+1}º número da lista2: ')))

    for item in range(0, 20):
        if item % 2 == 0:
            lista3.append(lista1[item])
        else:
            lista3.append(lista2[item])

    print(f'A primeira lista: {lista1}')
    print(f'A segunda lista: {lista2}')
    print(f'A terceira lista: {lista3}')

# # Exercício 9
def exercicio_9():
    print('=' * 30)
    print(f'{"Exercício 9":^30}')
    print('=' * 30)

    temp_media_mes = list()
    for mes in range(0, 12):
        temp_media_mes.append(float(input(f'Digite a temperatura média do {mes+1}º mês: [ºC] ')))

    media_anual = sum(temp_media_mes)/len(temp_media_mes)
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    print(f'A média de temperatura anual foi: {media_anual:.2f}')
    print('E os mêses acima da média foram')
    for mes in range(0, 12):
        if temp_media_mes[mes] >= media_anual:
            print(f'{meses[mes]}: {temp_media_mes[mes]}')

# # Exercício 10
def exercicio_10():
    from random import randint
    print('=' * 30)
    print(f'{"Exercício 10":^30}')
    print('=' * 30)

    acumulo = list()
    total = 50
    for rodada in range(0, total):
        acumulo.append(int(randint(1, 6)))

    for face in range(1, 7):
        vezes = acumulo.count(face)
        print(f'O número {face} saiu {vezes} vezes ou {(vezes/100*total):.2f} %')

# # Exercício 11
def exercicio_11():
    print('=' * 30)
    print(f'{"Exercício 11":^30}')
    print('=' * 30)
    
    questions = list()

    questions.append(str(input('Telefonou para a vítima: [S/N] ').upper().strip()[0]))
    questions.append(str(input('Esteve no local do crime: [S/N] ').upper().strip()[0]))
    questions.append(str(input('Mora perto da vítima: [S/N] ').upper().strip()[0]))
    questions.append(str(input('Devia para a vítima: [S/N] ').upper().strip()[0]))
    questions.append(str(input('Já trabalhou com a vítima: [S/N] ').upper().strip()[0]))

    resp_positivas = questions.count('S')
    classification = ''

    if resp_positivas == 2:
        classification = 'Suspeito'
    elif resp_positivas == 4 or resp_positivas == 3:
        classification = 'Cumplice'
    elif resp_positivas == 5:
        classification = 'Assassino'
    else:
        classification = 'Inocente'

    print(resp_positivas)
    print(questions)
    print(f'Você foi considerado {classification}')

# # Exercício 12
def exercicio_12():
    print('=' * 30)
    print(f'{"Exercício 12":^30}')
    print('=' * 30)

    votos = list()
    candidatos = ['Camila', 'Diego', 'Victor', 'Vinicius', 'Pedro']

    while True:
        finalizar = str(input('\nEm quem deseja votar: \n[Camila]\n[Diego]\n[Victor]\n[Vinicius]\n[Pedro]\n')).capitalize().strip()

        if finalizar in candidatos:  
            votos.append(finalizar)
        elif finalizar == 'Fim' or finalizar == '':
            break
        else:
            print('Voto em branco ou inválido, escolha uma opção correta!!!')

    print(f'Total de votos {len(votos)}')
    print('')
    campeao = 0
    campeao_nome = ''
    for pessoa in candidatos:
        print(f'{pessoa} recebeu {votos.count(pessoa)} votos, um total de {(votos.count(pessoa)/len(candidatos))*100:.2f}%')
        if votos.count(pessoa) > campeao:
            campeao_nome = pessoa
            campeao = votos.count(pessoa)
    print('')
    print(f'O campeão da votação foi {campeao_nome} com {votos.count(campeao_nome)} votos, um total de {(votos.count(campeao_nome)/len(candidatos))*100:.2f}%')

# # Exercício 13
def exercicio_13():
    print('=' * 30)
    print(f'{"Exercício 13":^30}')
    print('=' * 30)
    
    numeros = list()
    
    for n in range(0, 4):
        num = int(input('Digite um número: '))
        for index, valor in enumerate(numeros):
            if num < valor:
                numeros.insert(index, num)
                print(f'Foi inserido na posição {index}')
                break
        else:
            print(f'Foi inserido no fim da lista')
            numeros.append(num)
    print(numeros)
