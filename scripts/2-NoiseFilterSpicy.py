'''
Filtro Maximo con scipy
'''
import os
import numpy as np
import cv2 as cv
import scipy


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena_Ruido.jpg')
Img=cv.imread(filename,1)

'''cv.imshow('Lena Ruido', Img)'''
img_gray=cv.cvtColor(Img, cv.COLOR_BGR2GRAY)
Mask=7
a=scipy.ndimage.maximum_filter(img_gray,size=Mask)
b=scipy.ndimage.minimum_filter(img_gray,size=Mask)
c=scipy.ndimage.median_filter(img_gray,size=Mask)

cv.imshow('Lena - Filtro Minimo', b)
cv.imshow('Lena - Filtro Media', c)


cv.namedWindow('Lena - Color',cv.WINDOW_NORMAL)
cv.moveWindow('Lena - Color', 0,0,)
cv.arrowedLine(Img,(200,100),(400,300),(255,105,0),4)
cv.imshow('Lena - Color', Img)

cv.waitKey(0)
cv.destroyAllWindows()
