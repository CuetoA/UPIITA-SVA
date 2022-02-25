import numpy as np
import cv2 as cv

matriz = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

img1 = np.array(matriz)
img1 = np.uint8(img1)
print(img1)
print('Metodo 1')


img2 = np.zeros((5,4), np.uint8)
print(img2)
print('Metodo 2')

ancho = alto = 500
img3 = np.ones((alto, ancho), np.uint8) * 255
cv.imshow('Blanco', img3)
print('Método 3')


ancho = alto = 500
azul = np.ones((alto, ancho, 3), np.uint8) * 255
azul[:] = (255,0,0)
cv.imshow('Blanco', azul)
print('Método 4')


cv.waitKey(0)