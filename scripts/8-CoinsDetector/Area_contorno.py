import cv2 as cv
import numpy as np

Img = cv.imread('T04_DETECTOR_MONEDAS\PRUEBA_MONEDAS_1.jpg',1)
Img_color=Img.copy()
Img_gray=cv.cvtColor(Img,cv.COLOR_BGR2GRAY)

def Image_Binaria(Umbral):
	global Img_Binary
	_,Img_Binary=cv.threshold(Img_gray,Umbral,255,cv.THRESH_BINARY_INV)
	cv.imshow("Imagen Binaria",Img_Binary)

def Contornos():
	Contornos,_=cv.findContours(Img_Binary, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
	
	
	#for contorno in Contornos:				 #SE OMITIÓ LA IMPRESION
	#	print(cv.contourArea(contorno,True)) #COMPLETA DE LOS CONTORNOS
	#print("---------------------------------")
	
	vector=[] #SE CREÓ UN VECTOR PARA CONTENER LOS VALORES DE AREA
	for contorno in Contornos:
		vector.append(cv.contourArea(contorno,True))
	vector.sort(reverse=True) #SE ACOMODARON DE MAYOR A MENOR

	print(vector[0:7]) #SE IMRIMIERON LOS PRIMEROS SEIS VALORES

	Img=Img_color.copy()
	cv.drawContours(Img,Contornos,-1,(0,255,255),3)
	cv.imshow("Contornos",Img)

def actualizar_imagen(Umbral):
	Image_Binaria(Umbral)
	Contornos()

actualizar_imagen(0)

cv.createTrackbar("Umbral","Contornos",0,255,actualizar_imagen)

cv.waitKey(0)
cv.destroyAllWindows()