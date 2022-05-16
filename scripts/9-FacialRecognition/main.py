import os
import cv2 as cv
import numpy as np
import face_recognition


curentPath = os.getcwd()
completePath = f"{curentPath}/scripts/9-FacialRecognition/"
img1 = completePath + 'knownFacesDir/Andres/andres1.jpg'
img2 = img1
# knownFacesDir = completePath + "knownFacesDir"
# unknownFacesDir = completePath + "unknownFacesDir/this"
tolerance = 0.8
frameThikness = 3
fontThikness = 2
model = "cnn"  # convolutional neural network


andres_image = face_recognition.load_image_file(img1)
andres_facencoding = face_recognition.face_encodings(andres_image)[0]


known_face_encodings = [
    andres_facencoding,
]
known_face_names = [
    "La Cuetorra",
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

img = cv.imread(img2)
cv.imshow('test', img)
cv.waitKey(0)
cv.destroyAllWindows()