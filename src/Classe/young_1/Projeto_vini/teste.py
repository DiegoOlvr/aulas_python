import requests


def Pega_previsão(cidade: str):
    api_chave = '80bd52467da0e9b9e9d2288abbf9c23c'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_chave}'
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    temperatura = round(requisicao_dic['main']['temp'] - 273, 2)
    return temperatura


if __name__ == '__main__':
    api_chave = '80bd52467da0e9b9e9d2288abbf9c23c'
    cidade = 'Jundiaí'
    link = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_chave}'
    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    print(requisicao_dic)