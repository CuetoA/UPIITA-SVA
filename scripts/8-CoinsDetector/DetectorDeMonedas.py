import os
import cv2 as cv
import numpy as np
from Moneda import Moneda

class DetectorDeMonedas():


    def __init__(self):
        
        self.Umbral = 35
        self.grosor = 2
        self.color = (0,255,255)
        self.textSize = 1
        self.fuente = cv.FONT_HERSHEY_SIMPLEX
    
        n = 75
        self.moneda10p  = Moneda('Moneda $10', upperAreaLimit = 40000 +n, lowerAreaLimit = 36000 -n)
        self.moneda5p   = Moneda('Moneda $5', upperAreaLimit = 31522 +n, lowerAreaLimit = 31243 -n)
        self.moneda2p   = Moneda('Moneda $2', upperAreaLimit = 25738 +n, lowerAreaLimit = 25346 -n)
        self.moneda1p   = Moneda('Moneda $1', upperAreaLimit = 21283 +n, lowerAreaLimit = 21143 -n)
        self.moneda50c1 = Moneda('Moneda $0.5 tipo 1', upperAreaLimit = 23029 +n, lowerAreaLimit = 22768 -n)
        self.moneda50c2 = Moneda('Moneda $0.5 tipo 2', upperAreaLimit = 13758 +n, lowerAreaLimit = 13641 -n)
        
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
        img = cv.imread( self.filePath(fileName) ,1)
        imgColor = img.copy()
        imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        return imgColor, imgGray
    
    
    def filePath(self, fileName):    
        dirname = os.path.dirname(__file__)
        filePath = os.path.join(dirname , fileName)
        return filePath
    
    
    def getCountours(self, Img_gray):
        
        blur = cv.blur (Img_gray, (11,11))
        
        _ , thresh = cv.threshold(blur, self.Umbral, 255, cv.THRESH_BINARY_INV)
        #cv.imshow('Test', thresh)
        
        edges_high_thresh = cv.Canny(blur, 50, 50)
        #cv.imshow('canny', edges_high_thresh)
        
        _ , thresh2 = cv.threshold(edges_high_thresh, self.Umbral, 255, cv.THRESH_BINARY_INV)
        #cv.imshow('Test2', thresh2)
                
        
        size = (220, 220)
        Img_gray = cv.resize(Img_gray, size)
        thresh = cv.resize(thresh, size)
        edges_high_thresh = cv.resize(edges_high_thresh, size)
        thresh2 = cv.resize(thresh2, size)
        blur = cv.resize(blur, size)
        
        
        images = np.hstack((Img_gray, blur, thresh, edges_high_thresh, thresh2))
        cv.imshow('Frame', images)
        
        
        listaContornosAux , _ = cv.findContours(thresh2, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
        listaContornos, listaAreas = self.filterContoursAndGetArea(listaContornosAux)
        return listaContornos, listaAreas
    
    def filterContoursAndGetArea(self, listaContornosAux):
        listaContornos = []
        listaAreas = []
        for contorno in listaContornosAux:
            area = cv.contourArea(contorno)
            if  area > 1000 and area < 100000:
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
        ImgColor = cv.resize(ImgColor, (960, 540))
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