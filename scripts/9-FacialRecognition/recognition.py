import os
import cv2 as cv
from PIL import Image
import face_recognition


def encodingFaces():
    curentPath = os.getcwd()
    completePath = f"{curentPath}/scripts/9-FacialRecognition/"
    andres_imgf = completePath + 'knownFacesDir/Andres/andres1.jpg'
    scar_imgf = completePath + 'knownFacesDir/Scarlette/scar1.jpg'
    ceres_imgf = completePath + 'knownFacesDir/Ceres/ceres1.jpg'
    
    
    andres_image = face_recognition.load_image_file(andres_imgf)
    andres_facencoding = face_recognition.face_encodings(andres_image)[0]
    
    scar_image = face_recognition.load_image_file(scar_imgf)
    scar_facencoding = face_recognition.face_encodings(scar_image)[0]
    
    ceres_image = face_recognition.load_image_file(ceres_imgf)
    ceres_facencoding = face_recognition.face_encodings(ceres_image)[0]
    
    known_face_encodings = [scar_facencoding, ceres_facencoding, andres_facencoding]
    known_face_names = ["Scar", "Ceres", "Andres"]
       
    
    return known_face_encodings, known_face_names



def recognizingFaces(image, known_face_encodings, known_face_names):
    
    
    name           = "Unknown"
    face_names     = []
    face_locations = []
    face_encodings = []
    img            = image[:, :, ::-1]

    face_locations = face_recognition.face_locations(img)
    face_encodings = face_recognition.face_encodings(img, face_locations)

    for face_encoding in face_encodings:
        # # If a match was found in known_face_encodings, just use the first one.
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
        face_names.append(name)
        print(name)

    return face_locations, face_names



def displayResults(imgor, face_locations, face_names):
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
    imgor = cv.resize(imgor, dim)
    
    img = cv.cvtColor(imgor, cv.COLOR_BGR2RGB)
    img = Image.fromarray(img)    
    return img
    


