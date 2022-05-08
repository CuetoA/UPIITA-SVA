import cv2 as cv

class Filters():

    
    def __init__(self):
        self.filtersList = ['Canny']
    
    def canny(filename):
        img = cv.imread(filename)
        img_canny = cv.Canny(img, 50, 200, None, 3)
        return img_canny