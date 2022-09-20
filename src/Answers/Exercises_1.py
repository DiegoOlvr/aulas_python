# 1 - Faça um script que recebe duas informações do usuário (números inteiros) no qual um será o lado de uma figura germétrica e o outro a sua base. Com esses dois números apresente na saída a área de um triângulo, quadrado, retângulo, losangulo e trapézio. 
print('EXERCICIOS 1')
base = int(input("Digite o valor de uma base: "))
altura = int(input("Digite o valor para altura: "))
baseMenor = int(input("Digite uma base menor para o trapezio: "))

triangulo = (base*altura)/2
quadrado = (base*base)
retangulo = base*altura
losangulo = base*altura
trapezio = ((base + baseMenor) * altura)/2

print(f"\nA área do triângulo é: {triangulo:.1f} cm²\nA área do quadrado é: {quadrado:.1f} cm²\nA área do retângulo é: {retangulo:.1f} cm²\nA área do losangulo é: {losangulo:.1f} cm²\nA área do trapezio é: {trapezio:.1f} cm²")

# 2 - Faça um script que irá receber o montante de dinheiro a ser investido, quantidade de meses e a taxa de juros aplicada. Com isso retorne o valor que o usuário terá daqui a X meses mencionados. PS: utilizar a formula de juros simples.
print('\nEXERCICIOS 2')
montante = int(input("Digite o valor que será investido: "))
meses = int(input("Digite o total de meses: "))
taxa = int(input("Qua a taxa aplicada em porcentagem: ")) / 100

print(f"\nDaqui a {meses} meses você terá R$ {montante + (montante*meses*taxa):.2f}")

# 3 - Faça um programa que receba o número de um funcionário, a quantidade de horas q ele trabalhou e o valor que ele recebe por hora. Com isso retorne "O funcionário X trabalhou Y horas e recebeu R$ wwww,ww" lembrando q a apresentação do seu salário deve conter apenas duas casas decimais.
print('\nEXERCICIOS 3')
id = int(input("Digite o seu ID: "))
qtd_horas = int(input("Quantas horas vc trabalhou esse mês: "))
valor_horas = int(input("Qual o valor da sua hora de trabalho: "))

print(f"\nO funcionário {id} trabalhou {qtd_horas} horas e receberá R$ {(qtd_horas*valor_horas):.2f}")

# 4 - Escreva um script que converta a temperatura de graus Celsius para Fahrenheit.
print('\nEXERCICIOS 4')
celsius = int(input("Digite a temperatura em graus Celsius: "))

print(f"\nA temperatura em graus Fahrenheit é: {((celsius + (9/5))+32):.1f}")

# 5 - Desenvolva um programa que receba o valor do comprimento do cateto oposto e do cateto adjacente e retorne o comprimento da hipotenusa.
print('\nEXERCICIOS 5')
import math
oposto = int(input("Qual o comprimento do cateto oposto: "))
adjacente = int(input("Qual o comprimento do cateto adjacente: "))
hipotenusa = math.sqrt(((oposto**2)+(adjacente**2)))

print(f"\nO comprimento da hipotenusa desse triângulo é: {hipotenusa:.0f}")

# 6 - Crie um programa que irá receber um nome completo de uma pessoa. Esse programa deverá retornar o nome enviado em linhas diferentes (quebra de linha) todo maiúsculo, minúsculo, apenas com as iniciais maiúsculas, apenas com a primeira letra do nome completo todo maiúscula, o nome sem espaços (EX: DiegoRamos) e a terceira letra do primeiro nome.
print('\nEXERCICIOS 6')
nome = input("Digite o seu nome completo: ")

print(f'\nO seu nome é: {nome}\nMaiúsculo: {nome.upper()}\nMinúsculo: {nome.lower()}\nIniciais maiúsculas: {nome.title()}\nSó a primeira maiúscula: {nome.capitalize()}\nSem espaços: {nome.replace(" ", "")}\nTerceira letra do seu nome: {nome[2]}')