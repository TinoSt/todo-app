
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Liest eine Textdatei aus.
    :param filepath: Datentyp str, Pfad auf die Textdatei, default ist 'To-dos.txt'
    :return: Liste der To-dos
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Schreibt die Liste der To-dos in eine Textdatei.
    :param todos_arg: Liste der To-dos
    :param filepath: Pfad der Textdatei
    :return: None
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
