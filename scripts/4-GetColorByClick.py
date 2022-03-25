import os
import cv2 as cv

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena2.jpg')
img = cv.imshow('Color', filename)
img_copy = img.copy()

cv.imshow('Color', img_copy)

def color(event, x, y, flag, param):
    global img
    
    if event == cv.EVENT_LBUTTONDOWN:
        color = img[x.y] .tolist()
        pixel_radius = 40
        solid = -1
        cv.circle(img, (x,y), pixel_radius, color, solid)
        
    cv.imshow('Colores', img)
    
cv.setMouseCallback('Colores', color)
cv.waitKey(0)
cv.destroyAllWindows()
