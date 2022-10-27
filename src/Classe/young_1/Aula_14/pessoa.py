# A gente cria com a palavra class e passa o nome
from datetime import datetime


class Pessoa:
    # variáveis globais, que pertence a classe toda
    frase = 'Eu sou um serumanu!!!!'
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    # self = eu mesmo / o objeto instanciado 'clone'
    # Contrutor = Ele cria por padrão todo objeto assim

    def __init__(self, nome, ano, comendo=False, falando=False):
        # Características = atributos de cada objeto
        self.nome = nome
        self.nascimento = ano
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if not self.falando:
            self.comendo = True
            print(f'{self.nome} diz:')
            print(f'Estou comendo {alimento}')
            return
        else:
            print(f'{self.nome} está falando e por isso não pode comer')

    def falar(self, tema):
        if self.comendo:
            print(f'{self.nome} está comendo e por isso não pode falar :[')
            return
        print(f'{self.nome} diz:')
        print(f'Quero falar sobre {tema}')
        self.falando = True

    def desfalar(self):
        self.falando = False
        print('Parei de falar!!')

    def descomer(self):
        self.comendo = False
        print('Parei de comer hehe!!!')

    def idade(self):
        print(f'{self.nome} tem {Pessoa.ano_atual - self.nascimento} anos!!!')
