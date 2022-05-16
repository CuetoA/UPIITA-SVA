import face_recognition
import os
import cv2 as cv

curentPath = os.getcwd()
completePath = f"{curentPath}/scripts/9-FacialRecognition/"
knownFacesDir = completePath + "knownFacesDir"
unknownFacesDir = completePath + "unknownFacesDir/this"
tolerance = 0.8
frameThikness = 3
fontThikness = 2
model = "cnn"  # convolutional neural network


print("loading known faces")

knownFaces = []
knownNames = []



# Returns (R, G, B) from name
def name_to_color(name):
    # Take 3 first letters, tolower()
    # lowercased character ord() value rage is 97 to 122, substract 97, multiply by 8
    color = [(ord(c.lower())-97)*8 for c in name[:3]]
    return color




for name in os.listdir(knownFacesDir):
    # for filename in os.listdir(f"{knownFacesDir}/{name}"):
        
    #     print(filename)
        
    #     pass
    

    for filename in os.listdir(unknownFacesDir):
        
        # Load image
        print(f'Filename {filename}', end='')
        image = face_recognition.load_image_file(f'{unknownFacesDir}/{filename}')

        # This time we first grab face locations - we'll need them to draw boxes
        locations = face_recognition.face_locations(image, model=model)

        # Now since we know loctions, we can pass them to face_encodings as second argument
        # Without that it will search for faces once again slowing down whole process
        encodings = face_recognition.face_encodings(image, locations)

        # We passed our image through face_locations and face_encodings, so we can modify it
        # First we need to convert it from RGB to BGR as we are going to work with cv
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        # But this time we assume that there might be more faces in an image - we can find faces of diferent people
        print(f', found {len(encodings)} face(s)')
        for face_encoding, face_location in zip(encodings, locations):

            # We use compare_faces (but might use face_distance as well)
            # Returns array of True/False values in order of passed knownFaces
            results = face_recognition.compare_faces(knownFaces, face_encoding, tolerance)

            # Since order is being preserved, we check if any face was found then grab index
            # then label (name) of first matching known face withing a tolerance
            match = None
            if True in results:  # If at least one is true, get a name of first of found labels
                match = knownNames[results.index(True)]
                print(f' - {match} from {results}')

                # Each location contains positions in order: top, right, bottom, left
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])

                # Get color by name using our fancy function
                color = name_to_color(match)

                # Paint frame
                cv.rectangle(image, top_left, bottom_right, color, frameThikness)

                # Now we need smaller, filled grame below for a name
                # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)

                # Paint frame
                cv.rectangle(image, top_left, bottom_right, color, cv.FILLED)

                # Wite a name
                cv.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), fontThikness)

        # Show image
        scale_percent = 50 # percent of original size
        width = int(image.shape[1] * scale_percent / 100)
        height = int(image.shape[0] * scale_percent / 100)
        dim = (width, height)
        image = cv.resize(image, dim, interpolation=cv.INTER_AREA)
        cv.imshow(filename, image)
        cv.waitKey(0)
        cv.destroyWindow(filename)