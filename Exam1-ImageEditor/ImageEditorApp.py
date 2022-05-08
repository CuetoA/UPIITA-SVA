import io
import os
import PySimpleGUI as sg
from layout import layout
from PIL import Image
from Filters import Filters


fil = Filters()
window = sg.Window("Cueto's Image Editor", layout(fil.filtersList))





def printImage():
    image.thumbnail((400, 400))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["-IMAGE-"].update(data=bio.getvalue())


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Load Image':
        filename = values["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            printImage()
            
    if values['-FILTERS-']:
        print(f"Selected value: {values['-FILTERS-']}")
        print(f"Selected type: {type(values['-FILTERS-'])}")
        value = values['-FILTERS-']
        if value == 'Canny':
            image = fil.canny(filename)
            printImage()
            


window.close()