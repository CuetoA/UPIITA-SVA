import os
import math
import cv2 as cv
import numpy as np

color = (0, 0, 225)
thickness = 2
anchor_min = 125


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname , '../img/Lena2.jpg')
img = cv.imread(filename)
img_canny = cv.Canny(img, 50, 200, None, 3)

# line = cv.HoughLines(img_canny, 1,  np.pi/180, 150, None, 0, 0)

# if line is not None:
#     for i in range(0, len(line)):
#         rho = line[i][0][0]
#         theta = line[i][0][1]
#         a = math.cos(theta)
#         b = math.sin(theta)
#         x0 = a * rho
#         y0 = b * rho
#         pt1 = ( int(x0 + 1000 * b) , int(y0 + 1000 * a))
#         pt2 = ( int(x0 - 1000 * b) , int(y0 - 1000 * a))
#         cv.line(img_canny, pt1, pt2, (255,255,255), 3)

cv.imshow('Bordes', img_canny)
cv.waitKey(0)
cv.destroyAllWindows()