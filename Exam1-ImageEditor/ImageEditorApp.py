import io
import os
import PySimpleGUI as sg
from layout import layout
from PIL import Image

window = sg.Window("Cueto's Image Editor", layout())


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Load Image':
        filename = values["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-IMAGE-"].update(data=bio.getvalue())
    if values['-FILTERS-']:
        print(f"Selected value: {values['-FILTERS-']}")


window.close()