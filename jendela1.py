import PySimpleGUI as sg

sg.theme_text_color('#292d32')
texts = [
    [sg.Text("NPM : 2210010165")],
    [sg.Text("Nama : Muhammad Huda Mauladi")],
    [sg.Text("Kelas : TI 5O Reg Banjarmasin")],
    [sg.Text("Matkul : Visual 3")]
]

window = sg.Window(title='Latihan Pertama', layout=texts, size=(600, 300), font=('Georgia', 20))
window()
window.close()
