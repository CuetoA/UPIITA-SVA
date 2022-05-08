import PySimpleGUI as sg

file_types = [ ("JPEG (*.jpg)", "*.jpg") , ("All files (*.*)", "*.*") ]


def layout(mylist):
    
    column1 = [
        [sg.Image(key="-IMAGE-")]
    ]

    column2 = [
        [
            sg.Text("Image File"),
            sg.Input(size=(30, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types),
            sg.Button("Load Image"),
        ],
        [sg.Combo(mylist, enable_events=True, key='-FILTERS-')],
    ]

    layout = [
        [sg.Text("Welcome, select a file")],
        [sg.Column(column1),
        sg.Column(column2, key="-COLUMN2-")]
    ]
    
    
    return layout