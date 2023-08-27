
import functions
import PySimpleGUI as Sg

label = Sg.Text('Füge ein todo hinzu')
input_box = Sg.InputText(tooltip='Gib todo ein.', key='todo')
add_button = Sg.Button('add')

window = Sg.Window('Meine todo App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case Sg.WIN_CLOSED:
            break

window.close()
