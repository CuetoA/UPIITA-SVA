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
# Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
img = img[:, :, ::-1]

face_locations = face_recognition.face_locations(img)
face_encodings = face_recognition.face_encodings(img, face_locations)



face_names = []
name = "Unknown"
for face_encoding in face_encodings:
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    
    # # If a match was found in known_face_encodings, just use the first one.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]
        

    face_names.append(name)


# cv.imshow('test', img)
# cv.waitKey(0)
# cv.destroyAllWindows()