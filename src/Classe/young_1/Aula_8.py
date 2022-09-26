
# ! Funções
'''
Um conjunto de algoritmos que serão executados
print() => mostra algo no terminal ou output (saida)
len()
max(), min(), strip(),
função é como se fosse uma variável
ela armazena comandos

toda vez que formos usar uma função,
precisa por os parenteses
nome_da_função()

para criar as nossas funções
def = definir, nome da função, () e
dentro deles pode ter algo ou não
def nome_da_função(parametros*):

'''

# parametros / argumentos


def mult(n1: int, n2: int, n3: int, n4: int):
    resultado = int(n1) * int(n2)
    div = int(n3) / int(n4)
    fim = resultado + div
    return fim


# Argumentos posicionais
print(f'primeiro teste: {mult(3, 2, 2, 4)}')

# Argumentos nomeados
print(f'Segundo teste: {mult(3, n3=2, n2=2, n4=4)}')
print(f'Terceiro teste: {mult(2, 2, n4=3, n3=4)}')

# Argumentos predefinidos
# def prepararAcai(ing1: str, ing2: str, ing3: str, ing4: str = 'Açai'):
#     itens = list()
#     itens.append(ing1)
#     itens.append(ing2)
#     itens.append(ing3)
#     itens.append(ing4)
#     return itens
#     print('pudim')

# ingredientes = list()
# for i in range(3):
#     ingredientes.append(str(input('Digite um ingrediente: ')))


# pedido = prepararAcai(ingredientes[0], ingredientes[1], ingredientes[2])
# if pedido:
#     print('oi')
# else:
#     print(pedido)

# print('Seu açai contém: ')
# for item in pedido:
#     print(item)

# pedido = prepararAcai('banana', 'leite em pé', 'granola', 'sorvete')
# print('Seu açai contém: ')
# for item in pedido:
#     print(item)


# Argumentos arbitários = *args **kwargs
# # *args = argumentos multiplos / indefinidos
# ele vai jogar todos os seus parametros dentro de uma tupla
def preparar_acai(*ingredientes):
    print('O seu Açai contém: ')
    for item in ingredientes:
        print(item)


preparar_acai('Granola', 'Banana', 'Paçoca', 'Morango', 'leite em pó')
# print(pedido)
# print(pedido[3])

# # **kwagrs = argumentos multiplos / nomeados key words (palavras chaves)


def preparar_acai2(**ingredientes):
    print('O seu Açai_2 contém: ')
    for item in ingredientes:
        print(ingredientes[item])
    return ingredientes


preparo = preparar_acai2(ing1='Banana', ing2='Granola', ing3='Morango')
print(preparo)
print(type(preparo))

# * RECURSIVIDADEk
# fibonacci, fatorial
# função sem recursividade


def fatorial(num: int):  # 5! = 5 x 4 x 3 x 2 x 1 x 0 == 120
    if num < 0:
        print('Não existe fatorial de 0')
    elif num == 0:
        return 1
    else:
        resul = 1
        while (num > 1):
            resul *= num  # resul = resul * num
            num -= 1     # num = num - 1
        return resul


print(fatorial(5))
# função com recursividade
