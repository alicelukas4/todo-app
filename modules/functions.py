#FILEPATH = "../files/todos.txt"
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent   # project root
FILEPATH = BASE_DIR / "files" / "todos.txt"

def get_todos(filepath = FILEPATH):
    """Read a text file and return a list of todos items
    """
    with open(filepath,"r") as file:
        todos_l = file.readlines()
    return todos_l

def write_todos(todos_l, filepath = FILEPATH):
    """Write a list of todos items to a text file"""
    with open(filepath,"w") as file:
        #file.writelines(todos_l)
        file.writelines([str(item) for item in todos_l])

if __name__ == "__main__":
    print("hi")
    print(get_todos())