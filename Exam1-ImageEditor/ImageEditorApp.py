import io
import os
import PySimpleGUI as sg
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]

colum1 = [
    [sg.Text("Column1")],
    [sg.Image(key="-IMAGE-", size = (250, 250))],
]

colum2 = [
    [sg.Text("Column2")],
    [
        sg.Text("Image File"),
        sg.Input(size=(25, 1), key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Image"),
    ]
]

layout = [
    [sg.Text("Hello PySimpleGUI")],
    [sg.Column(colum1),
     sg.Column(colum2),
     ]
]


window = sg.Window("Hello", layout)

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
                
        print('Obrigado!')
        
        #window["-IMAGE-"].update(filename)

window.close()