#from functions import get_todos, write_todos
from modules import functions
import time

while True:
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print("It is", now)
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo+'\n')
        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}:{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number-1

            todos = functions.get_todos()
            edit = input("New value:")
            todos[number] = edit+'\n'
            functions.write_todos(todos)
        except ValueError:
            print("Your command isnt valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            todos.pop(number-1)
            functions.write_todos(todos)
        except IndexError:
            print("No item with that index")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("You have entered an invalid input")
print("Goodbye")

