from DetectorDeMonedas import DetectorDeMonedas
import cv2 as cv

def main():
    detector = DetectorDeMonedas()
    detector.detectCoins('monedasImgs\monedas00.jpeg')
    
    


if __name__ == "__main__":
    main()