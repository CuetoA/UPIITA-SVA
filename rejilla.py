import numpy as np
import cv2 as cv

color = [88, 24, 183]
width = high = 300
image = np.ones((high, width, 3), np.uint8) * 255

for x in range(width):
    for y in range(high):
        if x%50 == 0 or y%50 == 0:
            pointer = image[x,y]
            [pointer[0] , pointer[1] , pointer[2]] = color

cv.imshow('Rejilla', image)
cv.waitKey(0)