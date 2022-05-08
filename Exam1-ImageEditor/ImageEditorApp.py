import io
import os
import PySimpleGUI as sg
from PIL import Image

mylist = ['Scarlette', 'Andrés', 'Boni']

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

column1 = [
    [sg.Image(key="-IMAGE-")],
]

column2 = [
    [
        sg.Text("Image File"),
        sg.Input(size=(30, 1), key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Image"),
    ],
    [sg.Combo(mylist, enable_events=True, key='-FILTERS-')],
]

layout = [
    [sg.Text("Welcome, select a file")],
    [sg.Column(column1),
     sg.Column(column2, key="-COLUMN2-")]
]

window = sg.Window("Cueto's Image Editor", layout)




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