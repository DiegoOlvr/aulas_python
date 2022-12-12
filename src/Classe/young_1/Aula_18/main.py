import requests

# ! APIs
# link = 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,ARS-BRL'

# resposta = requests.get(link)
# cotacao = resposta.json()

# cotacao_dolar = cotacao['USDBRL']['bid']
# cotacao_euro = float(cotacao['EURBRL']['bid'])
# cotacao_peso_arg = float(cotacao['ARSBRL']['bid'])
#  cotacao_naira = float(cotacao['NGNBRL']['bid'])
# print(f'A cotação do Dolar - Real é R$ {float(cotacao_dolar):.2f}')
# print(f'A cotação do Euro - Real é: R$ {cotacao_euro:.2f}')
# print(f'A cotação do Peso Argentino - Real é: R$ {cotacao_peso_arg:.2f}')
#  print(f'A cotação do Naira - Real é: R$ {cotacao_naira:.2f}')


def pegar_cotacao(moeda: str):
    """Função para pegar a cotação mais recente
    da moeda escolhida em relação ao Real

    Args:
        moeda (str): Id da moeda

    Returns:
        valor (str): Valor cotado
    """
    link = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    respota = requests.get(link)
    cotacao = respota.json()
    chave = moeda + 'BRL'
    valor = cotacao[chave]['bid']
    return valor


if __name__ == '__main__':
    coin = input('Digite o cod da moeda: ').upper()
    resultado = pegar_cotacao(coin)
    print(resultado)
