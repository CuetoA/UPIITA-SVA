import PySimpleGUI as sg

file_types = [ ("JPEG (*.jpg)", "*.jpg") , ("All files (*.*)", "*.*") ]


def layout(mylist):
    
    column1 = [[sg.Image(key="-IMAGE-")]]

    column2 = [
        [
            sg.Text("Image File"),
            sg.Input(size=(30, 1), key="-FILE-")
        ],[
            sg.Text("               "),
            sg.FileBrowse(file_types=file_types, size=(10,1), target="-FILE-"),
            sg.Button("Load Image", size=(10,1)),
        ],[
            sg.Text("               "),
            sg.Combo(mylist, enable_events=True, key='-FILTERS-', size=(30,1))
        ],
    ]

    layout = [
        [sg.Text("Welcome, select a file")],
        [sg.Column(column1),
        sg.Column(column2, key="-COLUMN2-")]
    ]
    
    
    return layout