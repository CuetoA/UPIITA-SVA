import os
import cv2 as cv


class DetectorDeMonedas():
    def __init__(self):
        self.Monedas_10p=0
        self.Monedas_5p=0
        self.Monedas_2p=0
        self.Monedas_50c1=0
        self.Monedas_1p=0
        self.Monedas_50c2=0
        self.Umbral=35
        self.grosor=3
        self.color=(0,255,255)
        self.Posicion_texto_1=(10, 30)
        self.Posicion_texto_2=(10, 60)
        self.Posicion_texto_3=(10, 90)
        self.Posicion_texto_4=(10, 120)
        self.Posicion_texto_5=(10, 150)
        self.Posicion_texto_6=(10, 180)
        self.fuente=cv.FONT_HERSHEY_SIMPLEX
        
        
    def filePath(self, fileName):    
        dirname = os.path.dirname(__file__)
        filePath = os.path.join(dirname , fileName)
        return filePath
    
    def readImage(self, fileName):
        Img = cv.imread( self.filePath(fileName) ,1)
        Img_color=Img.copy()
        Img_gray=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)
        return Img_color, Img_gray
    
    def getCountours(self, Img_gray):
        _,Img_Binary=cv.threshold(Img_gray, self.Umbral, 255, cv.THRESH_BINARY_INV)
        listaContornos,_=cv.findContours(Img_Binary, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
        return listaContornos
    
    def countingCoins(self, listaContornos):    
        n=75
        
        for contorno in listaContornos:
            area=abs(cv.contourArea(contorno,True))

            if   area>=36000   and area<40000:      self.Monedas_10p  += 1
            elif area>=31243-n and area<31522+n:    self.Monedas_5p   += 1
            elif area>=25346-n and area<25738+n:    self.Monedas_2p   += 1
            elif area>=22768-n and area<23029+n:    self.Monedas_50c1 += 1
            elif area>=21143-n and area<21283+n:    self.Monedas_1p   += 1
            elif area>=13641-n and area<13758+n:    self.Monedas_50c2 += 1
        
    
    def printText(self, ImgColor):
        
        fuente = self.fuente
        color = self.color
        grosor = self.grosor
        cv.putText(ImgColor,"Moneda $10 =" + str(self.Monedas_10p), self.Posicion_texto_1,fuente,1,color,grosor)
        cv.putText(ImgColor,"Moneda $5 =" + str(self.Monedas_5p),self.Posicion_texto_2,fuente,1,color,grosor)
        cv.putText(ImgColor,"Moneda $2 =" + str(self.Monedas_2p),self.Posicion_texto_3,fuente,1,color,grosor)
        cv.putText(ImgColor,"Moneda $1 =" + str(self.Monedas_1p),self.Posicion_texto_5,fuente,1,color,grosor)
        cv.putText(ImgColor,"Moneda $50c =" + str(self.Monedas_50c1),self.Posicion_texto_4,fuente,1,color,grosor)
        cv.putText(ImgColor,"Moneda $50c chica =" + str(self.Monedas_50c2),self.Posicion_texto_6,fuente,1,color,grosor)
        return ImgColor
    
    def printImage(self, ImgColor):
        ImgColor = self.printText(ImgColor)
        cv.imshow("Coins Counter", ImgColor)
        cv.waitKey(0)
        cv.destroyAllWindows()