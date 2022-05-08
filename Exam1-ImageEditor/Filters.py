import cv2 as cv
from PIL import Image

class Filters:
    def __init__(self):
        self.filtersList = ['Canny']
        
    def decorateFunction(func):
        def wrapper(self, filename):
            img = cv.imread(filename)
            img = func(filename)
            return Image.fromarray(img)
            
        return wrapper
    
    @decorateFunction
    def canny(filename):
        img = cv.imread(filename)
        img_canny = cv.Canny(img, 50, 200, None, 3)
        return img_canny
    
    # @decorateFunction
    # def laplace(filename):
    #     ddepth = cv.CV_16S
    #     kernelSice = 7
        
    #     img1 = cv.imread(filename, 0) # 0 BN, 1 Color
    #     img1 = cv.Laplacian(img1 , ddepth, ksize = kernelSice )
    #     return img1