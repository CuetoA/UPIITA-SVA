import numpy as np
import cv2 as cv

ancho = alto = 300
rejilla = np.ones((alto, ancho), np.uint8) * 255
rejilla2 = np.ones((alto, ancho, 3), np.uint8) * 255

# Test
arreglo = rejilla2[0,0]
tipo = type(arreglo)
tamano = len(arreglo)
size2 = arreglo.size
print('\narreglo: {} \ntipo: {} \ntamaño: {} \nsize: {}'.format(arreglo,tipo,tamano, size2))

for x in range(ancho):
    for y in range(alto):
        if x%50 == 0 or y%50 == 0:
            rejilla2[x,y][0] = 88
            rejilla2[x,y][1] = 24
            rejilla2[x,y][2] = 183

cv.imshow('Rejilla', rejilla2)
cv.waitKey(0)