import os
import cv2 as cv
import numpy as np
import face_recognition

def recognizingFaces(img2, known_face_encodings, known_face_names):
    #   Empieza el reconocimiento de rostros


    face_locations = []
    face_encodings = []
    face_names = []

    imgor = img2
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    img = imgor[:, :, ::-1]

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
            print(name)

        face_names.append(name)

    return face_locations, face_names

    
    ###  Termina el reconocimiento



def displayResults(imgor, face_locations, face_names):
    # Display the results
    color = (0, 0, 255)
    font = cv.FONT_HERSHEY_DUPLEX
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Draw a box around the face
        cv.rectangle(imgor, (left, top), (right, bottom), color, 2)
        cv.rectangle(imgor, (left, bottom - 35), (right, bottom), color, cv.FILLED)
        cv.putText(imgor, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
    targetSize = 600
    height = imgor.shape[0]
    scale_percent = targetSize / height * 100
    
    
    width = int(imgor.shape[1] * scale_percent / 100)
    height = int(imgor.shape[0] * scale_percent / 100)
    dim = (width, height)

    # Display the resulting image
    imgor = cv.resize(imgor, dim)
    cv.imshow('test', imgor)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    
if __name__ == "__main__":
    
    ### Empieza a leer imágenes
    curentPath = os.getcwd()
    completePath = f"{curentPath}/scripts/9-FacialRecognition/"
    img1 = completePath + 'knownFacesDir/Scarlette/scar8.jpg'
    img2 = completePath + 'knownFacesDir/Scarlette/scar1.jpg'
    # knownFacesDir = completePath + "knownFacesDir"
    # unknownFacesDir = completePath + "unknownFacesDir/this"



    andres_image = face_recognition.load_image_file(img1)
    andres_facencoding = face_recognition.face_encodings(andres_image)[0]

    ## Termina de crear los encodings

    known_face_encodings = [
        andres_facencoding,
    ]
    known_face_names = [
        "Scar",
    ]
    
    imgor = cv.imread(img2)
    face_locations, face_names = recognizingFaces(imgor, known_face_encodings, known_face_names)
    displayResults(imgor, face_locations, face_names)
    