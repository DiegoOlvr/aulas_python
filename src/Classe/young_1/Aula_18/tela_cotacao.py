import PySimpleGUI as psg
from main import pegar_cotacao

moedas = [
    'AFN', 'MGA', 'THB', 'PAB', 'ETB', 'BTC', 'BOB', 'VEF', 'XBR', 'GHS',
    'SVC', 'CRC', 'CZK', 'DKK', 'ISK', 'NOK', 'SEK', 'NIO', 'SDR', 'GMD',
    'MKD', 'DZD', 'IQD', 'JOD', 'KWD', 'LYD', 'RSD', 'TND', 'BHD', 'MAD',
    'AED', 'STD', 'DOGE', 'VND', 'AMD', 'USD', 'AUD', 'CAD', 'JMD', 'NAD',
    'NZD', 'TWD', 'ZWL', 'BSD', 'KYD', 'BBD',  'BZD', 'BND', 'SGD', 'FJD',
    'HKD', 'TTD', 'XCD', 'CVE', 'ETH', 'EUR', 'HUF', 'BIF', 'XAF', 'XOF',
    'XPF', 'KMF', 'RWF', 'CHF', 'CHFRTS', 'GNF', 'DJF', 'HTG', 'PYG',
    'ANG', 'UAH', 'JPY', 'JPYRTS', 'PGK', 'LAK', 'HRK', 'MWK', 'ZMK',
    'AOA', 'MMK', 'GEL', 'ALL', 'HNL', 'MDL', 'RON', 'BGN', 'EGP', 'GBP',
    'LBP', 'SDG', 'SYP', 'SZL', 'LTC', 'LSL', 'AZN', 'BAM', 'MZN', 'MNT',
    'NGNPARALLEL', 'NGN', 'NGNI', 'TRY', 'ILS', 'MRO', 'MOP', 'ARS', 'CLP',
    'COP', 'CUP', 'DOP', 'PHP', 'MXN', 'UYU', 'BWP', 'GTQ', 'ZAR', 'BRL',
    'BRLT', 'QAR', 'IRR', 'OMR', 'KHR', 'MYR', 'YER', 'SAR', 'BYN', 'RUBTOM',
    'RUBTOD', 'RUB', 'MVR', 'IDR', 'INR', 'MUR', 'NPR', 'PKR', 'LKR', 'SCR',
    'KES', 'SOS', 'TZS', 'UGX', 'PEN', 'KGS', 'UZS', 'TJS', 'TMT', 'BDT',
    'KZT', 'VUV', 'KRW', 'XAGG', 'XRP', 'CNY', 'CNH', 'PLN'
]

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
