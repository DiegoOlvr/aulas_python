
from classe import Vendinha


v1 = Vendinha('Vans', 'sapatos', 'Roupas')
v2 = Vendinha('Saci Tintas', 'Todas_tintas', 'Quimicos')

print(f'Cadastrando produto para loja {v1.nome}')

lista_produtos = dict()

# for item in range(3):
#     nome = input('Digite o nome do produto com ID: ').strip().capitalize()
#     valor = input('Digite o valor do item: ').strip().capitalize()
#     lista_produtos[nome] = valor

lista_produtos = {
    '1 Salto Cinderela': 'R$250,00',
    '2 Pe de pato': 'R$80,00',
    '3 Air Jordan': 'R$350,00',
}

# v1.cadastrar(lista_produtos)
# v1.deletar('Pe de pato')
print('Consultado item')
v1.consultar_item('Salto Cinderela')
print('Consultando estoque')
v1.consultar_estoque()
