import os
import cv2 as cv
import numpy as np

ddepth = cv.CV_16S
kernelSice = 7

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena2.jpg')
img1 = cv.imread(filename, 0) # 0 BN, 1 Color
img1l = cv.Laplacian(img1 , ddepth, ksize = kernelSice )


cv.imshow('normal', img1)
cv.imshow('laplace', img1l)
cv.waitKey(0)