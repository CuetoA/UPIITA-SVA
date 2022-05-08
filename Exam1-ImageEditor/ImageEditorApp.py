import PySimpleGUI as sg

layout = [
    [sg.Text("Hello PySimpleGUI")],
    [sg.Button('E ai beleza')]
]

window = sg.Window("Hello", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'E ai beleza':
        print('Obrigado!')

window.close()