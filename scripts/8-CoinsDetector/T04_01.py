import cv2 as cv

Img = cv.imread('T04_DETECTOR_MONEDAS\monedas.jpg',1)
Img_color=Img.copy()
Img_gray=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)

"""
8862.5
6544.0
5045.5
"""
Area1=8700
Area2=6400
Area3=4900


Umbral=117
grosor=3
color=(0,255,255)
Posicion_texto_1=(10, 30)
Posicion_texto_2=(10, 60)
Posicion_texto_3=(10, 90)
fuente=cv.FONT_HERSHEY_SIMPLEX
Monedas_1=0
Monedas_2=0
Monedas_3=0

_,Img_Binary=cv.threshold(Img_gray, Umbral, 255, cv.THRESH_BINARY_INV)
Contornos,_=cv.findContours(Img_Binary, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

for contorno in Contornos:
    area=abs(cv.contourArea(contorno,True))

    if area>=Area1:Monedas_1+=1
    elif area>=Area2:Monedas_2+=1
    elif area>=Area3:Monedas_3+=1

cv.putText(Img,"Moneda 5 =" + str(Monedas_1),Posicion_texto_1,fuente,1,color,grosor)
cv.putText(Img,"Moneda 2 =" + str(Monedas_2),Posicion_texto_2,fuente,1,color,grosor)
cv.putText(Img,"Moneda 1 =" + str(Monedas_3),Posicion_texto_3,fuente,1,color,grosor)

cv.imshow("Contorno", Img)
cv.waitKey(0)
cv.destroyAllWindows()