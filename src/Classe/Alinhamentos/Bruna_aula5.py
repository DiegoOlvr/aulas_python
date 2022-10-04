
# ! DICIONÁRIOS

'''
Como criar um dicionário
livro = {chave: valor}
livro = dict()

Não permite duplicatas nas chaves
Não é "ordenado" = não ter indice
Pode ser mutável
'''


pessoas = {
    'Diego': 28,
    'Bruna': 17,
    'Camila': 14,
    'Victor': [16, 'victinho_milgrau@gmail.com', 'victor_o_bravo'],
}
nova_data = [25, 18, 24, 10]

# print(pessoas['Victor'])
# # RESOLVER DEPOIS
# for nome in pessoas:
#     if nome == 'Victor':
#         valores = pessoas[nome]
#         print(valores)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for indice, nome in enumerate(pessoas):
    pessoas.update({nome: nova_data[indice]})
    print(f'{nome} tem na vdd a idade: {nova_data[indice]}')

# pessoas.clear() => limpa o dicionário
# pessoas.pop('Diego') => remove o item
# pessoas.popitem() => remove o último
# pessoas.update({'Bruna': 27}) => para atualizar


# ! CONJUNTOS
'''
não pode conter duplicatas
não é ordenado
'''
conjuntinho = {'Cola', 'Tapioca', 'Biscoito'}
conjuntinho2 = {'Cola', 'Tapioca', 'Pão'}
conjuntinho.update(conjuntinho2)
print(conjuntinho)
print()

# ! FUNÇÕES
'''
conjunto de comando que fazem algo
print() => mostra o cod no terminal
'''
# b TODA VEZ QUE FOR CRIAR A SUA PRÓPRIA FUNÇÃO
# um padrão
'''
sempre começar com a palavra
def nome_da_funcao(por ou não argumentos):
    passa a ação dessa função
'''


# def preparar_acai(*item: str):
#     for ingrediente in item:
#         print(f'O seu açai contém: {ingrediente}')


def preparar_acai(item1: str, item2: str, item3: str):
    """Vai mostrar os itens coletados na função inicio

    Args:
        item1 (str): _description_
        item2 (str): _description_
        item3 (str): _description_
    """
    print(f'O seu açai tem: {item1}, {item2}, {item3}')


def inicio():
    """
    Ela pede ao usuário 3 ingredientes
    e usa a função preparar_acai
    """
    print('Bora lá preparar o seu açai!!!')
    ing1 = input('Digite o que vc deseja no seu acaizinho: ')
    ing2 = input('Digite o que vc deseja no seu acaizinho: ')
    ing3 = input('Digite o que vc deseja no seu acaizinho: ')
    # ing4 = input('Digite o que vc deseja no seu acaizinho: ')

    preparar_acai(ing2, item3=ing3, item2=ing1)  # argumentos nominais


inicio()
