from Filters import Filters
import io
import os
import PySimpleGUI as sg
from layout import layout
from PIL import Image

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
        value = values['-FILTERS-']
        if value == fil.filtersList[0]:      image = fil.canny(filename)
        if value == fil.filtersList[1]:      image = fil.laplace(filename)
        if value == fil.filtersList[2]:      image = fil.negative(filename)
        if value == fil.filtersList[3]:      image = fil.birghtAutoAdjust(filename)
        if value == fil.filtersList[4]:      fil.firstDerivate(filename)
        if value == fil.filtersList[5]:      fil.histogramsSelf(filename)
        
        printImage()

window.close()