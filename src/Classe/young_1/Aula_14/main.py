
from pessoa import Pessoa

# ! POO = Programação Orientada a Objetos
# b É como criar um molde de programação e pensar que o que vc criou
# b é um objeto

# # instanciar ou 'fazer um clone da classe'
# # instanciar = criar um objeto
p1 = Pessoa('Bruna', 2005)
p2 = Pessoa('Vinicius', 1940)
p3 = Pessoa('Victor', 2006)


print('\nFunção comer!!!')
p1.comer('Tapioca')
# p2.comer('Fini')
# p3.comer('Batata doce e Frango')

p1.descomer()
print('\nFunção falar!!!')
p1.falar('não sei kkkk')
# p3.falar('O mundial do Palmeiras')
# p2.falar('A volta de Bleach')

print('\nTeste do comer enquanto fala')
p1.desfalar()
p1.comer('Pão')

p1.idade()
p2.idade()
p3.idade()

print(p1.frase)
print(Pessoa.frase)
print(p1.ano_atual)
# print(Pessoa.nome) DÁ ERRO PQ NOME ESTÁ LIGADO A UM OBJETO
