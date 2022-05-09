import cv2 as cv
import numpy as np
from PIL import Image


def decorateFunction(func):
    def wrapper(self, filename):
        img = func(self, filename)
        return Image.fromarray(img)
        
    return wrapper
    

def separateAndJoinDecorator(func):
    def wrapper(self, filename):
        array = self.separateLayers(filename)
        func(self, filename)
        newArray = self.joinLayers(array)
        return newArray
    
    return wrapper


class Filters:
    def __init__(self):
        self.filtersList = ['Canny', 'Laplace', 'Complemento', 'test']
        
    
    @decorateFunction
    def canny(self, filename):
        img = cv.imread(filename)
        img_canny = cv.Canny(img, 50, 200, None, 3)
        return img_canny
    
    
    @decorateFunction
    def laplace(self, filename):
        img1 = cv.imread(filename, 0) # 0 BN, 1 Color
        img1 = cv.Laplacian(img1 , ddepth=cv.CV_16S , ksize = 7 )
        return img1
    
    
    @decorateFunction
    def complemento(self, filename):
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
    
    
    @decorateFunction
    @separateAndJoinDecorator
    def test(self, filename):
        print(f'Entramos dentro de test con el file: \n\t\t{filename}')
        
    
    def separateLayers(self, filename):
        
        img = cv.imread(filename)
        
        layer1 = []
        layer2 = []
        layer3 = []
        size = np.shape( img )
        rows   = size[0]
        columns = size[1]
          
        for row in range( rows ):
            rowL1 = []
            rowL2 = []
            rowL3 = []
            
            for column in range( columns ):
                pixelayerl = img[row][column][0]
                pixelLayer2 = img[row][column][1]
                pixelLayer3 = img[row][column][2]

                rowL1.append(pixelayerl)
                rowL2.append(pixelLayer2)
                rowL3.append(pixelLayer3)
                
            layer1.append(rowL1)
            layer2.append(rowL2)
            layer3.append(rowL3)
        
        imgByLayers = [layer1, layer2, layer3]
        imgaux = np.array( imgByLayers )        
        return imgaux
    
    
    def joinLayers(self, numpyArray):
        
        size = np.shape(numpyArray)
        rows    = size[1]
        columns = size[2]
        
        imgAux = []
        for row in range(rows):
            renglonAux = []
            for column in range( columns):
                p1 = numpyArray[2][row][column]
                p2 = numpyArray[1][row][column]
                p3 = numpyArray[0][row][column]
                columnaAux = [p1, p2, p3]
                renglonAux.append(columnaAux)
            imgAux.append(renglonAux)
        
        imgAux = np.array( imgAux )
        return imgAux      