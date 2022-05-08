import cv2 as cv
from PIL import Image

class Filters():

    
    def __init__(self):
        self.filtersList = ['Canny']
        
    def decorateFunction(func):
        def wrapper(filename):
            img = cv.imread(filename)
            img = func(filename)
            return Image.fromarray(img)
            
        return wrapper
    
    @decorateFunction
    def canny(filename):
        img = cv.imread(filename)
        img_canny = cv.Canny(img, 50, 200, None, 3)
        return img_canny