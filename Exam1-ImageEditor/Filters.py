import cv2 as cv
import numpy as np
from PIL import Image

class Filters:
    def __init__(self):
        self.filtersList = ['Canny', 'Laplace', 'Complemento']
        
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
    
    @decorateFunction
    def laplace(filename):
        ddepth = cv.CV_16S
        kernelSice = 7
        
        img1 = cv.imread(filename, 0) # 0 BN, 1 Color
        img1 = cv.Laplacian(img1 , ddepth, ksize = kernelSice )
        return img1
    
    @decorateFunction
    def complemento(filename):
        img = cv.imread(filename, 1)
        max = np.amax(img)
        size = np.shape( img )
        
        rowAux = []
        for row in range( size[0] ):
            columnAux = []
            for column in range( size[1] ):
                pixel = [ max - img[row][column][layer]  for layer in range( size[2] ) ]
                columnAux.append(pixel)
            rowAux.append(columnAux)
                
        return np.array( rowAux )
        