import os
import cv2 as cv
import numpy as np

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena2.jpg')
img = cv.imread(filename,1)
img = cv.imread(filename, 0) # 0 BN, 1 Color
cv.imshow('nombre', img)
cv.waitKey(0)

