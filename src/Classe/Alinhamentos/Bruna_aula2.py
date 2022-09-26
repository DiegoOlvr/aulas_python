
# # REVISÃO DA AULA PASSADA
# id = input('Digite a sua matricula')
# num = int(input('Quantas horas vc trabalhous: '))
# valor = int(input('Quanto vale a sua hora: '))

# print(f'O funcionário {id} trabalhou {num} horas
# e recebeu R$ {num*valor:.2f} reais')
# TC/5 = (TF – 32)/
# 9*(tc/5) = TF -32
# temperatura = int(input('Digite a temperatura em graus celcius: '))
# fahrenheit = 32 + (9*(temperatura/5))

# print(f'A temperatura {temperatura}ºC em Firenight é: {fahrenheit}')

# Manipulação de Strings / texto
'''
imutabilidade = não dá pra mudar depois de crido
\n \t len() split() strip() find() join() replace()
'''
#        01234 5 6789
nome = 'Diego Oliveira Ramos'
nome1 = 'Bruna Luchtenberg'
# START : STOP : STEP = por padrão ele entende que é 1
print(nome[6:14:2])
print(nome[-1::-1])

# * replace => realocar
print(nome.replace(' ', '-'))

# * tamanho de algo => len() length = comprimento
tam = len(nome1.replace(' ', ''))
print(f'Esse nome {nome1} tem {tam} letras')

# * split => fatiar
sem_especo = nome.split()
print(sem_especo)

# * find => encontar
print(nome1.find('B'))

# * join => juntar
print(''.join(sem_especo))

# ! Operadores de comparação
'''
> maior
< menor
>= maior ou igual
<= menor ou igual
== igualdade (dois iguais)
!= diferente (! mais =)

'''
print(nome > nome1)

# ! Operadores lógicos
'''
e = and precisa que as duas opções sejam verdadeira
ou = or precisa que uma das opções seja verdadeira
não = not negação ou inverso
'''
print(5 > 10 and 20 > 10)
print(5 > 10 or 20 > 10)
print(not False)

# ! Condicional simples
# se (condição):
#   faço a ação
# senão:
#   faço outra ação

if 5 > 10 and 20 > 10:
    print('parabéns')
else:
    print('deu ruim')

# ! Condicional composto
nota1 = int(input('Digite uma nota: '))
nota2 = int(input('Digite uma outra nota: '))
media = (nota1 + nota2) / 2
print(media)

if media >= 7:
    print('Passou raspando!')
elif media >= 5:
    print('Recuperação!')
else:
    print('Reprovou!')
