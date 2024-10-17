import PySimpleGUI as sg

sg.theme("DarkGreen4")
sg.theme_text_color('#fff')
layout = [
    [sg.Text("Teknologi Informasi", size=(25,1), justification="center")],
    [sg.Text("Teknologi Informasi", size=(25,1), justification="left")],
    [sg.Text("Teknologi Informasi", size=(25,1), justification="right")],
    [sg.Text(("Teknologi Informasi "+" ") * 2, size=(25,2), justification="center")],
    [sg.Text("Uniska MAB Banjarmasin", text_color="#fff00a")],
]

window = sg.Window(title='Profile', layout=layout, size=(1920, 1080), font=('Georgia', 20))
window()
window.close()
