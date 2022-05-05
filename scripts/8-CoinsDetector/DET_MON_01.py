import os
import cv2 as cv

def filePath(fileName):
    
    dirname = os.path.dirname(__file__)
    print(f'dirname: {dirname} \n')
    filePath = os.path.join(dirname , fileName)
    print(f'filename: {filePath} \n')
    return filePath

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
Monedas_1=0
Monedas_2=0
Monedas_3=0
Monedas_4=0
Monedas_5=0
Monedas_6=0

_,Img_Binary=cv.threshold(Img_gray, Umbral, 255, cv.THRESH_BINARY_INV)
Contornos,_=cv.findContours(Img_Binary, cv.RETR_LIST,cv.CHAIN_APPROX_NONE)

print(f'contornos: {Contornos}')

vector=[] #SE CRE� UN VECTOR PARA CONTENER LOS VALORES DE AREA
for contorno in Contornos:
	vector.append(cv.contourArea(contorno,True))
vector.sort(reverse=True) #SE ACOMODARON DE MAYOR A MENOR

#print(vector[0:6])
n=75

for contorno in Contornos:
    area=abs(cv.contourArea(contorno,True))

    if area>=36000 and area<40000:Monedas_1+=1
    elif area>=31243-n and area<31522+n:Monedas_2+=1
    elif area>=25346-n and area<25738+n:Monedas_3+=1
    elif area>=22768-n and area<23029+n:Monedas_4+=1
    elif area>=21143-n and area<21283+n:Monedas_5+=1
    elif area>=13641-n and area<13758+n:Monedas_6+=1


#[38266, 31522, 25738, 23029, 21283, 13758
#[37887, 31243, 25346, 22768, 21143, 13641

cv.putText(Img,"Moneda $10 =" + str(Monedas_1),Posicion_texto_1,fuente,1,color,grosor)
cv.putText(Img,"Moneda $5 =" + str(Monedas_2),Posicion_texto_2,fuente,1,color,grosor)
cv.putText(Img,"Moneda $2 =" + str(Monedas_3),Posicion_texto_3,fuente,1,color,grosor)
cv.putText(Img,"Moneda $1 =" + str(Monedas_5),Posicion_texto_5,fuente,1,color,grosor)
cv.putText(Img,"Moneda $50c =" + str(Monedas_4),Posicion_texto_4,fuente,1,color,grosor)
cv.putText(Img,"Moneda $50c chica =" + str(Monedas_6),Posicion_texto_6,fuente,1,color,grosor)

cv.imshow("Contorno", Img)
cv.waitKey(0)
cv.destroyAllWindows()