import os
import cv2 as cv
import numpy as np
from Moneda import Moneda

class DetectorDeMonedas():


    def __init__(self):
        
        self.Umbral = 35
        self.grosor = 1
        self.color = (0,255,255)
        self.textSize = 0.5
        self.fuente = cv.FONT_HERSHEY_SIMPLEX
    
        tolerance = 75
        self.moneda10p  = Moneda('Moneda $10', avrgArea = 2039, areaTolerance = tolerance )
        self.moneda5p   = Moneda('Moneda $5', avrgArea = 1701, areaTolerance = tolerance )
        self.moneda2p   = Moneda('Moneda $2', avrgArea = 1391, areaTolerance = tolerance )
        self.moneda1p   = Moneda('Moneda $1', avrgArea = 1156, areaTolerance = tolerance )
        self.moneda50c1 = Moneda('Moneda $0.5 tipo 1', avrgArea = 1246, areaTolerance = tolerance )
        self.moneda50c2 = Moneda('Moneda $0.5 tipo 2', avrgArea = 760, areaTolerance = tolerance )
        
        self.coinsObjectList = [self.moneda10p, self.moneda5p,   self.moneda2p,
                                self.moneda1p,  self.moneda50c1, self.moneda50c2]
        
    
    def detectCoins(self, filename):
        Img_color, Img_gray = self.readImage(filename)
        listaContours, listaAreas = self.getCountours(Img_gray=Img_gray)
        print(f'\nLista Areas: \n{len(listaAreas)}')
        print(f'Lista Areas: \n{listaAreas}\n')
        self.countingCoins(listaAreas)
        cv.drawContours(Img_color, listaContours, -1, (0,255,0), 3)
        self.printImage(Img_color)
        
        
    def readImage(self, fileName):
        path = self.filePath(fileName)
        print(f'\n este: {path}\n')
        img = cv.imread( self.filePath(fileName) ,1)
        imgColor = img.copy()
        imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        return imgColor, imgGray
    
    
    def filePath(self, fileName):    
        dirname = os.path.dirname(__file__)
        filePath = os.path.join(dirname , fileName)
        return filePath
    
    
    def getCountours(self, Img_gray):
        
        _ , thresh = cv.threshold(Img_gray, self.Umbral, 255, cv.THRESH_BINARY_INV)
        listaContornosAux , _ = cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
        listaContornos, listaAreas = self.filterContoursAndGetArea(listaContornosAux)
        return listaContornos, listaAreas
    
    
            
            
            
    
    def filterContoursAndGetArea(self, listaContornosAux):
        listaContornos = []
        listaAreas = []
        for contorno in listaContornosAux:
            area = cv.contourArea(contorno)
            if  area > 1 and area < 100000:
                listaContornos.append(contorno)
                listaAreas.append(area)
        
        return listaContornos, listaAreas
    
    
    def countingCoins(self, listaAreas): 
           
        for Area in listaAreas:
            self.checkAreaPertenence(Area)
            
                            
    def checkAreaPertenence(self, area):
        for moneda in self.coinsObjectList:
            if  area< moneda.upperAreaLimit and area >= moneda.lowerAreaLimit:
                moneda.quantity += 1
                break
        
    
    def printImage(self, ImgColor):
        ImgColor = self.printText(ImgColor)
        #ImgColor = cv.resize(ImgColor, (960, 540))
        cv.imshow("Coins Counter", ImgColor)
        cv.waitKey(0)
        cv.destroyAllWindows()
        
    
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