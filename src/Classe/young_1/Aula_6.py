
# ! REVISÃO AULA PASSADA

votos = list()
participantes = ['Camila', 'Diego', 'Victor', 'Vinicius', 'Pedro']

while True:
    candidato = str(input('Deseja votar em quem \n[Camila]\n[Diego]\n[Vitor]\n[Vinicius]\n[Pedro]\n:')).capitalize().strip()
    
    if candidato in participantes:
        votos.append(candidato)
    elif candidato == 'Fim':
        break
    else:
        print('Voto em branco ou inválido!!, escolha uma opção correta')


print(f'A quantidade de votos computados foi: {len(votos)}')
nome_vencedor =''
vencedor = 0
for pessoa in participantes:
    print(f'{pessoa} teve {votos.count(pessoa)} votos um total de {votos.count(pessoa)/len(votos)*100:.2f}%')
    if votos.count(pessoa) > vencedor:
        vencedor = votos.count(pessoa)
        nome_vencedor = pessoa

print(f'\nO vencedor foi: {nome_vencedor}')




# ! CONJUNTOS
'''
serve para obter algo que não queremos duplicado, e extrair informação em comum
habitantes = set() ou 
habitantes = {'diego', 'vinicius', 2, [1, 2, 3]}
construtor = set()
unordered = não tem indice ou seja, é aleatório o armazenamento dele
unchangeable* = não consigo mudar os itens dentro dela, mas eu consigo remover e adicionar 
duplicates not allowed não aceita duplicatas

métodos

add (add(), update()), 
remove (remove(), discard(), pop(), clear()), 
join (union(), update(), intersection(), symmetric_difference())

'''

habitantes = {'diego', 'camila', 'victor', 'vinicius', 'pedro', 'diego'}
print(habitantes)

if 'diego' in habitantes:
    habitantes.remove('diego')
else:
    print('não tem')
print(habitantes)
habitantes.add('renato')
print(habitantes)
habitantesM = {'diego', 'renato', 'joao'}
habitantes.update(habitantesM)
deletado = habitantes.pop()
deletado2 = habitantes.discard('jason')
print(deletado)
print(deletado2)
print(habitantes)


comunidade1 = {'pao', 'arroz', 'feijao'}
comunidade2 = {'pao', 'macarrao', 'oleo'}
# union retorna a união de dois sets
#print(comunidade1.union(comunidade2))
# o q tem em comum entre eles
#print(comunidade1.intersection(comunidade2))
# retorna o contrário da intersecção
#print(comunidade1.symmetric_difference(comunidade2))
'''
o discart se não houver o item buscado
ele não faz nada 
não devolve um erro
'''

# ! DICIONARIOS
'''
key/'chave' = value/'valor'

farofa = 'descrição do que significa'

construtor = dict()
## unordered or ordered
não possui indices, mas conseguimos encontrar os item dentro dele
pela chave ou pelo valor
## changeable 
pode ser alterado
duplicates not allowed

métodos

access (nome_do_dicionario['key'], get(), keys(), values(), items() )
change(update(), )
add(update(), )
remove(pop(), popitem(), clear(), )
loop
copy(copy(), dict())

'''
comidas = {
    'farofa': 'um tipo de farinha de milho usado no churras',
    'pimenta': 'um vegetal picante',
    'arroz': 'um tipo de cereal',
    }
    
print(comidas)
print('')
print(comidas.keys())
print('')
print(comidas.values())
print('')
print(comidas.items())
print('')

comidas['arroz'] = 'é um alimento que acompanha o feijão'
comidas.update({'arroz': 123})
#comidas.clear() deleta tudo do dicionario
#comidas.pop('feijão')
dicionario1 = comidas # não posso copiar um dicionario assim
# pq ele cria uma referencia, ou seja, tudo oq vc alterar no comidas 
# tbm vai ser alterado dicionario1
dicionario1.copy(comidas)
print(comidas)

#lista = list()
#lista.append(comidas.items())
#print(lista)