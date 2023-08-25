
import functions
import time

now = time.strftime("%d.%m.%Y, %H:%M:%S")
print(f"Heute ist der {now}\n")

while True:
    user_action = input("Gib 'plus', 'anzeigen', 'bearbeiten', 'erledigt' oder 'schließen' ein: ")
    user_action = user_action.strip()

    if user_action.startswith("plus"):
        todo = user_action[5:]

        todos = functions.get_todos()
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("anzeigen"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("bearbeiten"):
        try:
            number = int(user_action[11:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Gib bearbeitetes todo ein: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Dein Befehl ist nicht korrekt.")
            continue

    elif user_action.startswith("erledigt"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Das todo '{todo_to_remove}' wurde aus der Liste entfernt."
            print(message)
        except IndexError:
            print("Falsche Nummer.")
            continue

    elif user_action.startswith("schließen"):
        break

    else:
        print("Dein Befehl ist nicht korrekt.")

print("Und Tschüss!")
