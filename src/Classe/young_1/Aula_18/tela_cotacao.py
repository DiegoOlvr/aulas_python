import PySimpleGUI as psg
from main import pegar_cotacao

moedas = [
    'AFN',
    'MGA',
    'THB',
    'PAB',
    'ETB',
    'BTC',
    'BOB',
    'VEF',
    'XBR', 'GHS', 'SVC', 'USD', 'AUD', 'CAD', 'ETH', 'EUR', 'CHF']

# Escolhendo o tema
psg.theme('DarkPurple6')

# ! 1ª etapa = Criar o layout da janela
layout = [
    [psg.Text('Moeda '), psg.Combo(moedas, key='MOEDA', size=(14, 0))],
    [psg.Output(size=(22, 5))],
    [psg.HSep()],
    [psg.Push(), psg.Button('Enviar', key='ENVIAR'), psg.Push()],
]

# ! 2ª etapa = Abrir a janela com o layout
window = psg.Window('Cotação de Moedas', layout, finalize=True)


# ! 3ª etapa = Ler o conteudo da janela
while True:
    evento, valor = window.read()
    moeda = valor['MOEDA']
    if evento == 'ENVIAR':
        valor_cotado = pegar_cotacao(moeda)
        print(f'A cotação da moeda {moeda} em Reais é {valor_cotado}')
    if evento == psg.WIN_CLOSED:
        break
window.close()
