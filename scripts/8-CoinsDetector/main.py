import cv2 as cv
import numpy as np
from DetectorDeMonedas import DetectorDeMonedas

def main():
    detector = DetectorDeMonedas()
    img1 = detector.detectCoins('monedas1bl.JPG', returnImage = True)
    img2 = detector.detectCoins('monedas2bl.JPG', returnImage = True)
    img3 = detector.detectCoins('monedas3bl.JPG', returnImage = True)
    
    size = img1.shape
    size = (size[0] , size[1])
    img1 = cv.resize(img1, size)
    img2 = cv.resize(img2, size)
    img3 = cv.resize(img3, size)
    images = np.hstack((img1, img2, img3))
    
    cv.imshow('Coins counter', images)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()