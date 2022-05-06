import cv2 as cv
from DetectorDeMonedas import DetectorDeMonedas

def main():
    detector = DetectorDeMonedas()
    img1 = detector.detectCoins('monedas1bl.JPG', returnImage = True)
    img2 = detector.detectCoins('monedas2bl.JPG', returnImage = True)
    img3 = detector.detectCoins('monedas3bl.JPG', returnImage = True)



    cv.imshow("Coins Counter", ImgColor)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()