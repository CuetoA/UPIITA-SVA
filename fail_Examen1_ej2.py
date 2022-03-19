from turtle import shape
import cv2 as cv
import numpy as np

sol=cv.imread('sol.jpg',0)
cv.imshow("Sol",sol)

luna=cv.imread('luna.jpg',0)
cv.imshow("Luna",luna)

alfa=0.05
heightS, widthS =sol.shape[:2] 
heightL, widthL =luna.shape[:2]

M_min=min(heightS,heightL)
N_min=min(widthS,widthL)
I=[]

newA = int
newB = []
newC = []

i = 0
j = 0

for j in range(N_min):
    for i in range(M_min):
        
        print("data: {} \t type: {}".format(alfa, type(alfa)))
        print("data: {} \t type: {}".format(sol[i,j], type(sol[i,j])))
        print("data: {} \t type: {}".format(luna[i,j], type(luna[i,j])))
        
        
        newA = int(alfa)
        newB[i,j] = int(sol[i,j])
        newC[i,j] = int(luna[i,j])
        
        # print("addres newB {} \t addres sol {}".format(id(newB) , id(sol) )  )

        print("tipo: ", type(alfa))
        print("tipo: ", type(newB[i,j]))
        print("tipo: ", type(newC[i,j]))

        I[i,j]=(1-alfa)*sol[i,j] + alfa*luna[i,j]

cv.imshow(I)


cv.waitKey(0)
cv.destroyAllWindows()
print(M_min)
