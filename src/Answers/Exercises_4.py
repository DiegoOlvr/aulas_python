import os

os.system('cls')
espacamento = 25
print('=' * 30)
print('Cadastro de clientes')
print('=' * 30)

fatA = 0
fatB = 54000

for cliente in range(1, 6):
    fatA += int(input(f"Insira o valor da compra do {cliente}º cliente: "))

if fatA > fatB:
    print(f'O faturamento da loja A superou em R$ {fatA - fatB:.2f}')
else:
    print('A loja A não superou a loja B!')

for i in range(0, espacamento):
    print('')

# * exercicio 2
print('=' * 30)
print('Separador de par e impar')
print('=' * 30)

limite = int(input('Digite até onde deseja a sequência: '))
pares = list()
impares = list()
for numero in range(1, limite+1):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Pares: {pares}')
print(f'Impares: {impares}')

for i in range(0, espacamento):
    print('')

# * exercicio 3
print('=' * 30)
print('Média aritimética')
print('=' * 30)

cont = total = 0
while True:
    num = int(input('Digite um número: '))
    if num >= 0:
        total += num
        cont += 1
    else:
        break

media = total / cont if cont > 0 else total
print(f'A média aritimética foi: {media}')

for i in range(0, espacamento):
    print('')

# * exercicio 4
print('=' * 30)
print('Contador de negativos')
print('=' * 30)

cont = 0
for i in range(1, 6):
    num = int(input(f'Digite o {i}º número: '))
    if num < 0:
        cont += 1

print(f'Tivemos {cont} valores negativos')

for i in range(0, espacamento):
    print('')

# * exercicio 5
print('=' * 30)
print('Quantidade de vogais')
print('=' * 30)

palavra = str(input('Digite uma palavra: ')).lower().strip()
qtd_vogais = 0
vogais = 'aeiou'

while palavra[0] != 'd':
    for letra in palavra:
        if letra in vogais:
            qtd_vogais += 1
    print(f'{palavra} possui {qtd_vogais} vogais')
    qtd_vogais = 0

    palavra = str(input('Digite uma nova palavra: ')).lower().strip()
print('Fim do programa, vc digitou uma palavra com inicial D')

for i in range(0, espacamento):
    print('')

# * exercicio 6
print('=' * 30)
print('Média de idades digitadas')
print('=' * 30)

media = cont = 0

while True:
    idade = int(input('Digite uma idade: '))
    if idade != 0:
        media += idade
        cont += 1
    else:
        break

print(f'A média das idades foi: {media/cont:.2f}')

for i in range(0, espacamento):
    print('')

# * exercicio 7
print('=' * 30)
print('Contador de características')
print('=' * 30)
print('Olhos = [A – Azul, P- Preto, V- Verde e C- Castanho]')
print('Cabelos = [P – Preto, C- Castanho, L – Louro e R-Ruivo]')

qtd_analizada = 2
analise1 = analise2 = somaIdade = contOlhos = contador = 0

for pessoa in range(1, qtd_analizada+1):
    print('')
    idade = int(input(f'Digite a idade da {pessoa}ª pessoa: '))
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: ').replace(',', '.'))
    altura = float(input(f'Digite a altura da {pessoa}ª pessoa: ').replace(',', '.'))
    olhos = input(f'Digite a cor de olhos da {pessoa}ª pessoa: ').upper().split()
    cabelos = str(input(f'Digite a cor dos cabelos da {pessoa}ª pessoa: ')).upper().split()

    if peso < 60 and idade > 50:
        analise1 += 1
    if altura < 1.50:
        somaIdade += idade
        contador += 1
    if olhos[0][0] == 'A':
        contOlhos += 1
    if cabelos[0][0] == 'R' and olhos[0][0] != 'A':
        analise2 += 1
print('')
print(f'A quantidade de pessoas com mais de 50 anos e menos que 60 KG: {analise1}\n')
print(f'A média de idade das pessoas com menos de 1,50 cm: {somaIdade/contador:.2f}\n')
print(f'A porcentagem de pessoas com olhos azuis: {(contOlhos*100)/qtd_analizada:.2f} %\n')
print(f'A quantidade de pessoas ruivas que não tem olhos azuis: {analise2}\n')

for i in range(0, espacamento):
    print('')

# * exercicio 8
print('=' * 30)
print('Ordenador')
print('=' * 30)

recebidos = ''
for vez in range(1, 4):
    num = input('Digite um número: ')
    recebidos += num

print(recebidos)
print(sorted(recebidos, reverse=True))
print(sorted(recebidos))



# # COM LISTA
valores = list()

for i in range(1, 4):
    num = int(input('Insira um valor inteiro: '))
    valores.append(num)


print(f'Ordem enviada: {valores}')
print(f'Crescente: {valores.sort()}')
print(f'Decrescente: {valores.sort(reverse= True)}')

for i in range(0, espacamento):
    print('')

# * exercicio 9
# . 0 - 1 - 1 - 2 - 3 - 5 - 8
print('=' * 30)
print('Fibonacci')
print('=' * 30)

t1 = 0
t2 = 1

qtd_fibonacci = int(input('Digite quantos termos de fibonacci deseja ver: '))
cont = 1

while  cont < qtd_fibonacci+1:
    if cont == 1:
        print(f'{t1}', end='')
        cont += 1
    elif cont == 2:
        print(f' => {t2}', end='')
        cont += 1
    else:
        tn = t1 + t2
        print(f' => {tn}', end='')
        t1 = t2
        t2 = tn
        cont += 1

for i in range(0, espacamento):
    print('')

