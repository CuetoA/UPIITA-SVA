import os
import cv2 as cv

color = (0, 0, 255)
thick = 2
min_with = 100

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena2.jpg')
img = cv.imread(filename, 1)
img_copy = img.copy()
cv.imshow('Cuadro', img)

def region(event, x, y, flags, param):
    global x1, y1, img
    
    if event == cv.EVENT_LBUTTONDOWN:
        x1, y1 = x, y 
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        img  = img_copy.copy()
        first_coordenate = (x1,y1)
        current_coordenate = (x,y)
        cv.rectangle(img, first_coordenate , current_coordenate, color, thick)
    elif event == cv.EVENT_LBUTTONUP:
        if abs(x-x1) > min_with:
            
            y_arr = [y, y1]
            y_start = min(y_arr)
            y_end = max(y_arr)
            
            x_arr = [x, x1]
            x_start = min(x_arr)
            x_end = max(x_arr)
            
            img_cut = img_copy[y_start:y_end , x_start:x_end]
            cv.imshow('Snippset', img_cut)
    cv.imshow('Cuadro', img)
    
cv.setMouseCallback('Cuadro', region)
cv.waitKey(0)
cv.destroyAllWindows()
        