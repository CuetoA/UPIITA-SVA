import cv2 as cv
import numpy as np

img = cv.imread('formas-colores.jpg',1)
cv.imshow('nombre', img)

b,g,r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)


cv.waitKey(0)