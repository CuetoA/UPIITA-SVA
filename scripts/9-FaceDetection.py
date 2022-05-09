import os
import cv2 as cv

color = (0, 255, 255)
grosor = 2
escala = 1


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena2.jpg')
img = cv.imread(filename)

clasficador = cv.CascadeClassifier('base de datos que no descargué')
grayImg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
caras = clasficador.detectMultiscale(grayImg)

for (x, y, ancho, alto) in caras:
    cv.rectangle(img, (x,y), (x+ancho, y+alto), color, grosor)
    
cv.imshow('Rostros', img)
cv.waitKey(0)
cv.destroyAllWindows()