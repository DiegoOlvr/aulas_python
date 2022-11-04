
class Cartao:
    def __init__(self, nome: str, bandeira, limite, validade: str, cds):
        self.nome = nome
        self.bandeira = bandeira
        self.limite = limite
        self.validade = validade
        self.cvc = cds

    # GETTERS = Pegar / obter

    @property
    def limite(self):
        return self._limite
    # SETTERS = Configurar / definir

    @limite.setter
    def limite(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._limite = valor

    def mostrar_limite(self):
        print(f'O cartão do {self.nome} tem R$ {self.limite} de limite')

    def mostrar_info(self):
        print(f'O cartão do {self.nome} tem a bandeira {self.bandeira}')
        print(f'Tem a validade {self.validade} e limite de R$ {self.limite}')

    def comprar(self, produto, preco):
        if self.limite < preco:
            print('Saldo insuficiente')
        else:
            print(f'Você comprou {produto} de R$ {preco}!!!')
            self.limite -= preco
            self.registra_compra(produto, preco)

    def registra_compra(self, produto, preco):
        with open('fatura', 'a+') as arquivo:
            arquivo.write(f'{produto}, {preco}\n')

    def mostrar_fatura(self, arquivo):
        print(f'A fatura do {self.nome}')
        with open(arquivo, 'r') as file:
            tudo = file.readlines()

        for item in tudo:
            print(item.replace('\n', ''))
