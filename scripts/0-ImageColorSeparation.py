import os
import cv2 as cv
import numpy as np

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/formas-colores.jpg')
img = cv.imread(filename,1)
cv.imshow('nombre', img)

b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)


cv.waitKey(0)