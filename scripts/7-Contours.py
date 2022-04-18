import os
import cv2 as cv

dirname     = os.path.dirname(__file__)
filename    = os.path.join(dirname , '../img/formas-colores.jpg')
img         = cv.imread(filename, 1)
imgCopy     = img.copy()    
img_gray    = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def binaryImage(umbral):
    global img_umbral
    _,img_umbral = cv.threshold(img_gray, umbral, 255, cv.THRESH_BINARY_INV)
    cv.imshow("Umbral Image", img_umbral)

def contorno():
    color       = (0, 255, 255)
    contorno,_  = cv.findContours(img_umbral, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    img         = imgCopy.copy()
    cv.drawContours(img, contorno, -1, color, 2)  
    cv.imshow("Contours", img)

def updateImage(umbral):
    binaryImage(umbral)
    contorno()
    
updateImage(0)

cv.createTrackbar('umbral', "Contours", 0, 255, updateImage)
cv.waitKey(0)
cv.destroyAllWindows()