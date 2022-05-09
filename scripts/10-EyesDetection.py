import os
import cv2 as cv

color = (0, 255, 255)
grosor = 2
escala = 1


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena2.jpg')
img = cv.imread(filename)

clasficadorCaras = cv.CascadeClassifier('base de datos que no descargué')
grayImg = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
caras = clasficadorCaras.detectMultiscale(grayImg)

for (x, y, ancho, alto) in caras:
    cv.rectangle(img, (x,y), (x+ancho, y+alto), color, grosor)
    clasificadorOjos = cv.CascadeClassifier('base de datos que no descargué de ojos')
    cara = grayImg[y:y+alto, x:x+ancho]
    ojos = clasificadorOjos.detectMultiscale(cara, scaleFactor = 1.1, minNeighbors = 10, minSize = (20,20) )
    
    for (x1, y1, ancho1, alto1) in ojos:
        radio = int( (ancho1 + alto1)/4 )
        cv.circle(img, (x1+x+radio , y1+y+radio), radio, color, grosor )
        
    
cv.imshow('Rostros', img)
cv.waitKey(0)
cv.destroyAllWindows()