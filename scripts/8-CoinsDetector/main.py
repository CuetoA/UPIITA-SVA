from DetectorDeMonedas import DetectorDeMonedas
import cv2 as cv

def main():
    detector = DetectorDeMonedas()
    detector.detectCoins()
    
    


if __name__ == "__main__":
    main()