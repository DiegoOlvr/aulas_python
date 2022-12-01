import PySimpleGUI as sg
from time import sleep


def criar_janela():
    sg.theme('DarkBlue1')

    layout = [
        [sg.Push(), sg.Button(
            'Começar Contargem',
            size=(10, 0),
            key='-RUN-'), sg.Push()],
        [sg.Output(size=(20, 10))],
    ]

    window = sg.Window('Contagem Ano Novo', layout, finalize=True)

    return window


def contagem():
    for count in range(10, -1, -1):
        print(count)
        sleep(0.5)
    print('FELIZ ANO NOVO!!!')


window = criar_janela()

while True:
    event, value = window.read()

    if event == '-RUN-':
        contagem()
    elif event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
