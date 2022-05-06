from DetectorDeMonedas import DetectorDeMonedas
import cv2 as cv

def main():
    detector = DetectorDeMonedas()
    detector.detectCoins('monedas1bl.JPG')
    
    


if __name__ == "__main__":
    main()