import os
from bleach import clean
import cv2 as cv

flag = False

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena.jpg')
img = cv.imread(filename)
img_copy = img.copy()


cv.imshow('Color', img_copy)

def color(event, x, y, flag, param):
    global img
    
    if event == cv.EVENT_LBUTTONDOWN:
        flag = True
        makeCircle(x, y)
    elif event == cv.EVENT_MOUSEMOVE and flag:
        cleanImage()
        makeCircle(x, y)
    elif event == cv.EVENT_LBUTTONUP:
        flag = False
        cleanImage()
    cv.imshow('Color', img)
    
def makeCircle(x, y):
    color = img[x , y].tolist()
    pixel_radius = 40
    solid = -1
    cv.circle(img, (x,y), pixel_radius, color, solid)

def cleanImage():
    global img
    img = img_copy.copy()
    
cv.setMouseCallback('Color', color)
cv.waitKey(0)
cv.destroyAllWindows()
