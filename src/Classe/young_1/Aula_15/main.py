
from cartaozinho import Cartao

Diego = Cartao('Diego', 'Master', 'R$2000', '10/27', 454)
Victor = Cartao('VICTOR', 'visa', 5000, '08/30', 175)

print('---Objeto Diego---')
Diego.mostrar_info()
Diego.comprar('60 Ovos', 25)
Diego.comprar('Feijão', 8)
Diego.comprar('Coca', 5)
Diego.comprar('Tapioca', 16)
Diego.mostrar_fatura('fatura')
print(Diego.limite)
# print(Diego.limite)
Diego.mostrar_limite()

print('\n---Objeto Victor---')
print(Victor.nome, Victor.limite)
print(Victor.mostrar_limite())
Victor.mostrar_info()

'''
# # Modificadores de acesso
Pro python, tudo é publico

public => publico = tudo
protect => protegido = _ (underline)
    Se vc vê algo com underline, vc não deveria mexer nisso

private => privado = __ (dois underlines)
    Mesmo se vc tentar alterar um parametro com 2 underlines
    o python não deixará e ele irá criar um parametro novo
    com o mesmo nome que tem lá na classe

    O único que pode alterar, é a própria classe
'''
