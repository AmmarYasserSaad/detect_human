import PySimpleGUI as sg
from PIL import Image
from detection import det_hum
import os
import io

layout=[
    [sg.Text('choose image'),sg.Input(),sg.FileBrowse(key="-file-")],
    [sg.Button('Submit'),sg.Button("Detect")],
    [sg.Image(key="-image-")],
    [sg.Text(key='-text-')]  
]
window=sg.Window("detection",layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event =='Exit':
        break
    if event == 'Submit':
        print(values)
        if os.path.exists(values["-file-"]):
            image= Image.open(values["-file-"])
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            image.save(bio, format="PNG")
            window["-image-"].update(data=bio.getvalue())
    if event == 'Detect':
        print(values)
        image=det_hum(values['-file-'])
        image= Image.open(image)
        image.thumbnail((400, 400))
        bio = io.BytesIO()
        image.save(bio, format="PNG")
        print(image)
        window["-image-"].update(data=bio.getvalue())