
# ! estruturas de repetição


'''
for = para
while = enquanto


# # SINTAX DO FOR
FOR "UMA VARIÁVEL" IN "INTERVÁLO (range)":
lembrando que o interválo (start, stop, step)

quando eu uso o for???
quando eu tenho um limite já pensado



'''
nome = str(input('Digite o seu nome: '))
for numero in range(1, 11):
    if numero == 7:
        continue
    if numero == 5:
        pass
    print(numero)

for indice in range(0, len(nome)):
    print(nome[indice])
    print('não acabou')
print('fim do for')

condicao = True
while condicao:
    num = int(input('Digite um número: '))
    if num < 0:
        condicao = False
        pass # passar 
        continue # continuar
else:
    print('terminei o while')

'''
pedir um número qualquer positivo, e mostrar 
os números pares dele 
ex: 15
0 - 15 
e so mostre os pares
0 2 4 6 8 10 12 14
'''
# 0 1 6
soma = 0 
for i in range(0, 11):
    if i % 2 == 0:
        soma = soma + i # soma += i 
        print(f'{soma} e {i}')