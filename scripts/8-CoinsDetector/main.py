from DetectorDeMonedas import DetectorDeMonedas
import cv2 as cv

def main():
    detector = DetectorDeMonedas()
    
    Img_color, Img_gray = detector.readImage('PRUEBA_MONEDAS_2.jpg')
    
    cv.imshow("Contorno", Img_color)
    cv.imshow("Contorno2", Img_gray)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()