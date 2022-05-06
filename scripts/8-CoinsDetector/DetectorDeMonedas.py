import os
import cv2 as cv
from Moneda import Moneda

class DetectorDeMonedas():


    def __init__(self):
        
        self.createCoins()
        self.Umbral = 35
        self.grosor = 2
        self.color = (0,255,255)
        self.textSize = 1
        self.fuente = cv.FONT_HERSHEY_SIMPLEX
    
    def detectCoins(self):
        Img_color, Img_gray = self.readImage('PRUEBA_MONEDAS_2.jpg')
        listaContours = self.getCountours(Img_gray=Img_gray)
        self.countingCoins(listaContours)
        self.printImage(Img_color)
        
        
    def createCoins(self):
        n = 75
        self.moneda10p  = Moneda('Moneda $10', upperAreaLimit = 40000 +n, lowerAreaLimit = 36000 -n)
        self.moneda5p   = Moneda('Moneda $5', upperAreaLimit = 31522 +n, lowerAreaLimit = 31243 -n)
        self.moneda2p   = Moneda('Moneda $2', upperAreaLimit = 25738 +n, lowerAreaLimit = 25346 -n)
        self.moneda1p   = Moneda('Moneda $1', upperAreaLimit = 21283 +n, lowerAreaLimit = 21143 -n)
        self.moneda50c1 = Moneda('Moneda $0.5 tipo 1', upperAreaLimit = 23029 +n, lowerAreaLimit = 22768 -n)
        self.moneda50c2 = Moneda('Moneda $0.5 tipo 2', upperAreaLimit = 13758 +n, lowerAreaLimit = 13641 -n)
        
        self.coinsObjectList = [self.moneda10p, self.moneda5p,   self.moneda2p,
                                self.moneda1p,  self.moneda50c1, self.moneda50c2]
        
        
        
    def filePath(self, fileName):    
        dirname = os.path.dirname(__file__)
        filePath = os.path.join(dirname , fileName)
        return filePath
    
    
    def readImage(self, fileName):
        img = cv.imread( self.filePath(fileName) ,1)
        imgColor = img.copy()
        imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        return imgColor, imgGray
    
    
    def getCountours(self, Img_gray):
        _ , imgBinary = cv.threshold(Img_gray, self.Umbral, 255, cv.THRESH_BINARY_INV)
        listaContornos , _ = cv.findContours(imgBinary, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
        return listaContornos
    
    
    def countingCoins(self, listaContornos):    
        for contorno in listaContornos:
            area = abs( cv.contourArea( contorno , True ) )
            self.checkAreaPertenence(area)
            
                            
    def checkAreaPertenence(self, area):
        for moneda in self.coinsObjectList:
            if  area< moneda.upperAreaLimit and area >= moneda.lowerAreaLimit:
                moneda.quantity += 1
                break
        
    
    def printText(self, ImgColor):
        
        x = 10
        y = 30
        fuente = self.fuente
        color = self.color
        grosor = self.grosor
        size = self.textSize
        
        for moneda in self.coinsObjectList:  
            y += 30
            position = (x , y)
            cv.putText(ImgColor, self.generateText(moneda), position, fuente, size, color, grosor)
        
        return ImgColor


    def generateText(self, moneda):
        return moneda.name + ': ' + str( moneda.quantity )
           
    
    def printImage(self, ImgColor):
        ImgColor = self.printText(ImgColor)
        cv.imshow("Coins Counter", ImgColor)
        cv.waitKey(0)
        cv.destroyAllWindows()