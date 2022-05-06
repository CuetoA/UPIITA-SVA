import os
import cv2 as cv

def filePath(fileName):
    
    dirname = os.path.dirname(__file__)
    filePath = os.path.join(dirname , fileName)
    return filePath

def contourArea(listaContornos):
    areasVector=[] #SE CRE� UN VECTOR PARA CONTENER LOS VALORES DE AREA
    for contorno in listaContornos:
        areasVector.append(cv.contourArea(contorno,True))
    areasVector.sort(reverse=True) #SE ACOMODARON DE MAYOR A MENOR
    return areasVector


def countingCoins(coinsList):    
    n=75
    Monedas_10p=0
    Monedas_5p=0
    Monedas_2p=0
    Monedas_50c1=0
    Monedas_1p=0
    Monedas_50c2=0
    
    
    for contorno in Contornos:
        area=abs(cv.contourArea(contorno,True))

        if   area>=36000 and area<40000:Monedas_10p+=1
        elif area>=31243-n and area<31522+n:Monedas_5p+=1
        elif area>=25346-n and area<25738+n:Monedas_2p+=1
        elif area>=22768-n and area<23029+n:Monedas_50c1+=1
        elif area>=21143-n and area<21283+n:Monedas_1p+=1
        elif area>=13641-n and area<13758+n:Monedas_50c2+=1
    
    return Monedas_10p, Monedas_5p, Monedas_2p, Monedas_50c1, Monedas_1p, Monedas_50c2

############## EMPIEZA PROGRAMA

Img = cv.imread( filePath('PRUEBA_MONEDAS_2.jpg') ,1)
Img_color=Img.copy()
Img_gray=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)

"""
38190.0
31460.0
25696.5
22997.5
21257.5
13733.0
"""

Umbral=35
grosor=3
color=(0,255,255)
Posicion_texto_1=(10, 30)
Posicion_texto_2=(10, 60)
Posicion_texto_3=(10, 90)
Posicion_texto_4=(10, 120)
Posicion_texto_5=(10, 150)
Posicion_texto_6=(10, 180)
fuente=cv.FONT_HERSHEY_SIMPLEX
Monedas_10p=0
Monedas_5p=0
Monedas_2p=0
Monedas_50c1=0
Monedas_1p=0
Monedas_50c2=0
coinsList = [Monedas_10p, Monedas_5p, Monedas_2p, Monedas_50c1, Monedas_1p, Monedas_50c2]



_,Img_Binary=cv.threshold(Img_gray, Umbral, 255, cv.THRESH_BINARY_INV)
Contornos,_=cv.findContours(Img_Binary, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

#print(f'contornos: {Contornos}')
areasVector = contourArea(Contornos)

Monedas_10p, Monedas_5p, Monedas_2p, Monedas_50c1, Monedas_1p, Monedas_50c2 = countingCoins(coinsList)




#[38266, 31522, 25738, 23029, 21283, 13758
#[37887, 31243, 25346, 22768, 21143, 13641

cv.putText(Img,"Moneda $10 =" + str(Monedas_10p),Posicion_texto_1,fuente,1,color,grosor)
cv.putText(Img,"Moneda $5 =" + str(Monedas_5p),Posicion_texto_2,fuente,1,color,grosor)
cv.putText(Img,"Moneda $2 =" + str(Monedas_2p),Posicion_texto_3,fuente,1,color,grosor)
cv.putText(Img,"Moneda $1 =" + str(Monedas_1p),Posicion_texto_5,fuente,1,color,grosor)
cv.putText(Img,"Moneda $50c =" + str(Monedas_50c1),Posicion_texto_4,fuente,1,color,grosor)
cv.putText(Img,"Moneda $50c chica =" + str(Monedas_50c2),Posicion_texto_6,fuente,1,color,grosor)

cv.imshow("Contorno", Img)
cv.waitKey(0)
cv.destroyAllWindows()