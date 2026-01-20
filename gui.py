from modules import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True,size=(45,10))
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App",
                   layout=[[label],[input_box, add_button],[list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "todos":  # user clicked an item in listbox
            window["todo"].update(values["todos"][0].strip())
        case "Add":
            todos=functions.get_todos()
            new_todo = values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update("")
        case "Edit":
            selected_index = window['todos'].get_indexes()[0]
            new_todo = values['todo']+'\n'

            todos = functions.get_todos()
            todos[selected_index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED:
            break
window.close()