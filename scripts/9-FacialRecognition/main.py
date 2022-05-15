#import face_recognition
import os
#import cv2 as cv

curentPath = os.getcwd()
completePath = f"{curentPath}/scripts/9-FacialRecognition/"
knownFacesDir = completePath + "knownFacesDir"
unknownFacesDir = completePath + "unknownFacesDir"
tolerance = 0.6
frameThikness = 3
fontThikness = 2
model = "cnn"  # convolutional neural network


print("loading known faces")

knownFaces = []
knownNames = []





for name in os.listdir(knownFacesDir):
    for filename in os.listdir(f"{knownFacesDir}/{name}"):
        
        print(filename)
        
        pass