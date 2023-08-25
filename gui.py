
import functions
import PySimpleGUI as Sg

label = Sg.Text('Füge ein todo hinzu')
input_box = Sg.InputText(tooltip='Gib todo ein.')
add_button = Sg.Button('Hinzu')

window = Sg.Window('Meine todo App', layout=[[label], [input_box, add_button]])
# wenn label und input_box in einer eigenen Liste stehen, werden sie in einer Zeile abgebildet.
window.read()  # display the Window on the screen
window.close()
