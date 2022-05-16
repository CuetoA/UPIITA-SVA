import PySimpleGUI as sg

file_types = [ ("JPEG (*.jpg)", "*.jpg") , ("All files (*.*)", "*.*") ]


def layout(miLista):
    
    column1 = [[sg.Image(key="-IMAGE-")]]

    column2 = [
        [
            sg.Text("               "),
            sg.Combo(miLista, enable_events=True, key='-IMAGES-', size=(30,1))
        ],
        [
            sg.Button('Process', size=(10,1) )
        ]
    ]

    layout = [
        [sg.Text("Welcome, select a file")],
        [sg.Column(column1),
        sg.Column(column2, key="-COLUMN2-")]
    ]
    
    
    return layout