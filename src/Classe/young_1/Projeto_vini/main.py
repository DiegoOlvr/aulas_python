import PySimpleGUI as psg
from teste import Pega_previsão

layout = [
    [psg.Text('Previsão do tempo')],
    [psg.Text('Cidade'), psg.Input(key='CIDADE')],
    [psg.Button('Ver Previsão do Tempo')],
    [psg.Output(size=(100, 100))],
    ]

janela = psg.Window('Previsão Do tempo.', layout, finalize=True, size=(300, 300))

while True:
    evento, valor = janela.read()
    if evento == 'Ver Previsão do Tempo':
        cidade = valor['CIDADE']
        temperatura = Pega_previsão(cidade)
        print(f'A Temperatura em {cidade} é de {temperatura} Cº')

    if evento == psg.WIN_CLOSED:
        break

janela.close()
