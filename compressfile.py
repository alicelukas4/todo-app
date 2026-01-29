import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout = [
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [compress_button, output_label]
                   ])
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == "Compress":
        files_value = values.get("files", "")
        folder = values.get("folder", "")

        if not files_value or not folder:
            window["output"].update("Pick files + a folder first.")
            continue
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window["output"].update(value="Compressed!")
        print(filepaths)
        print(folder)


window.close()