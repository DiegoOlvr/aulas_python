import PySimpleGUI as sg

# https://www.pysimplegui.org/en/latest/#pypi-statistics-versions
sg.theme('DarkPurple1')
# # Criando o layout da janela
layout = [
    [sg.Text('Nome ', size=(5, 0)), sg.Input(key='-NOME-', size=(15, 0))],
    [sg.Text('Idade ', size=(5, 0)), sg.Input(key='-IDADE-', size=(15, 0))],
    [sg.HSep()],
    [sg.Output(size=(40, 10))],
    [sg.Push(), sg.Button('Enviar', size=(7, 0)), sg.Push()],
]

# # Criando a janela
window = sg.Window('Janelinha com Python', layout)

# ! Para fazer a janela aparecer, preciso usar o .read()
while True:
    # # Ler as informações da janela
    event, value = window.read()
    nome = str(value['-NOME-']).capitalize()
    idade = int(value['-IDADE-'])
    print(f'Você inseriu o usuário {nome} com {idade} anos!!!')

    # ! Para fechar a janela
    if event == sg.WIN_CLOSED:
        break

window.close()
