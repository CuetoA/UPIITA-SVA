import os
import cv2 as cv


class DetectorDeMonedas():
    def __init__(self):
        Monedas_10p=0
        Monedas_5p=0
        Monedas_2p=0
        Monedas_50c1=0
        Monedas_1p=0
        Monedas_50c2=0
        
        
    def filePath(self, fileName):    
        dirname = os.path.dirname(__file__)
        filePath = os.path.join(dirname , fileName)
        return filePath
    
    def readImage(self, fileName):
        Img = cv.imread( self.filePath(fileName) ,1)
        Img_color=Img.copy()
        Img_gray=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)
        return Img_color, Img_gray