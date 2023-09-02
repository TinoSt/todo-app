
import functions
import PySimpleGUI as Sg
import time
import os


if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

Sg.theme('DarkBlack')

clock_label = Sg.Text("", key='clock')
label = Sg.Text('Füge ein todo hinzu')
input_box = Sg.InputText(tooltip='Gib todo ein.', key='todo')
add_button = Sg.Button('add')
list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 12])

edit_button = Sg.Button('edit')
complete_button = Sg.Button('complete')
exit_button = Sg.Button('exit')

window = Sg.Window('Meine todo App',
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%d.%m.%Y, %H:%M Uhr'))
    match event:
        case 'add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup('Please select an item first.', font=('Helvetica', 14))
        case 'complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                Sg.popup('Please select an item first.', font=('Helvetica', 14))
        case 'exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case Sg.WIN_CLOSED:
            break

window.close()
