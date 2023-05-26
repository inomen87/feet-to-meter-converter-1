import PySimpleGUI as sg
from convert_engine import conversion


sg.theme("DarkGreen6")

label1 = sg.Text("Enter feet")
input1 = sg.Input()
# button1 = sg.FilesBrowse("Choose", key="files")


label2 = sg.Text("Enter inches")
input2 = sg.Input()
# button2 = sg.FolderBrowse("Choose", key="folder")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")


exit_button = sg.Button("Exit")

window = sg.Window("Feet2meter converter", layout=[[label1, input1], [label2, input2], [convert_button, exit_button, output_label]])



while 1:
	event, values = window.read()

	match event:
		case "Convert":
			print(event, values)
			feet = values[0]
			inches = values[1]
			window["output"].update(value=conversion(feet, inches))


		case "Exit":
			break


		case sg.WIN_CLOSED:
			break

window.close()