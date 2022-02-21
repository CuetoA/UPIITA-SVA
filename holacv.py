import cv2 as cv
import numpy as np

img = cv.imread('./Lena2.jpg', 0) # 0 BN, 1 Color
cv.imshow('nombre', img)
cv.waitKey(0)

