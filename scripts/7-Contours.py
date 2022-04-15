import os
import cv2 as cv

umbral = 200
color = (0, 255, 255)

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/formas-colores.jpg')
img = cv.imread(filename, 1)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_,img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY_INV)

contorno,_ = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, contorno, -1, color, 2)

cv.imshow('Colores', img)  
cv.waitKey(0)
cv.destroyAllWindows()