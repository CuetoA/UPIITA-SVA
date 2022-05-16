import io
import os
import cv2 as cv
from PIL import Image
import PySimpleGUI as sg
from layout import layout
import recognition as rc

def printImage(image):
    image.thumbnail((400, 400))
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    window["-IMAGE-"].update(data=bio.getvalue())







if __name__ == '__main__':
        
    completePath = f"{os.getcwd()}/scripts/9-FacialRecognition/imgs/"
    imgsList = os.listdir(completePath)
    window = sg.Window("Cueto's Image Editor", layout(imgsList))

    known_face_encodings, known_face_names = rc.encodingFaces()




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
            
            image = cv.imread(filename)
            face_locations, face_names = rc.recognizingFaces(image, known_face_encodings, known_face_names)
            rc.displayResults(image, face_locations, face_names)
            


    window.close()