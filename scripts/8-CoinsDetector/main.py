from DetectorDeMonedas import DetectorDeMonedas
import cv2 as cv

def main():
    detector = DetectorDeMonedas()
    detector.detectCoins('PRUEBA_MONEDAS_2.jpg')
    
    


if __name__ == "__main__":
    main()