
# b CLASSES NÃO MOLDES !!!

class Vendinha():
    def __init__(self, nome, arquivo, area_comercial) -> None:
        self.nome = nome
        self.estoque = arquivo
        self.area_comercial = area_comercial

    def cadastrar(self, produtos):
        dict_de_produtos = produtos

        for produto, valor in dict_de_produtos.items():
            aux = str(produto)
            id = aux[:2]
            prod = aux[2:]
            with open(self.estoque, 'a+') as f:
                f.write(f'{id} {prod} {valor}\n')

    def deletar(self, produto):
        # item que quero deletar
        item = produto
        # Abrir o arquivo para ler
        with open(self.estoque, 'r') as f:
            linhas = f.readlines()
            # Abri o arquivo para sobrescrever
            with open(self.estoque, 'w+') as f:
                for linha in linhas:
                    # Se o arquivo não está na linha
                    if item not in linha:
                        # Reescreve a linha
                        f.write(f'{linha}')

    def atualizar(self):
        pass

    def consultar_estoque(self):
        with open(self.estoque, 'r') as f:
            linhas = f.readlines()
            for linha in linhas:
                print(linha)

    def consultar_item(self, produto):
        item = produto
        with open(self.estoque, 'r') as f:
            linhas = f.readlines()
            for linha in linhas:
                if item in linha:
                    print(linha)


class Produto():
    def __init__(self, ID, nome, valor) -> None:
        self.id = ID
        self.nome = nome
        self.valor = valor
