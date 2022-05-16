import io
import os
from PIL import Image
import PySimpleGUI as sg
from layout import layout


curentPath = os.getcwd()
completePath = f"{curentPath}/scripts/9-FacialRecognition/imgs/"
imgsList = os.listdir(completePath)
window = sg.Window("Cueto's Image Editor", layout(imgsList))



def printImage(image):
    image.thumbnail((400, 400))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["-IMAGE-"].update(data=bio.getvalue())


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
            
    if values['-IMAGES-']:
        value = values['-IMAGES-']
        print(f'\nSelected value: {value}')
        filename = completePath + value
        
        if os.path.exists(filename):
            image = Image.open(filename)
            printImage(image)
            
    if event == 'Process':
        print('process')
        


window.close()