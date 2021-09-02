import PySimpleGUI as sg

from utils.process import Process

class GuiApplication():
    def __init__(self):
        self.setting = True
        self.layout = [
            [sg.Text('File', size=(15, 1)), sg.Input(), sg.FileBrowse('select file.', key='file')],
            [sg.Text('Base', size=(15, 1)),sg.Combo(('color', 'object'), default_value='color',size=(10, 1), key='base')],
            [sg.Text('Color', size=(15, 1)),sg.Combo(('red', 'blue', 'green', 'orange'), default_value='red',size=(10, 1), key='color')],
            [sg.Text('Inversion', size=(15, 1)),sg.Combo(('yes', 'no'), default_value='no',size=(10, 1), key='inv')],
            [sg.Button('start!', key='start')]]

    def apps(self):
        sg.theme('Black')

        window = sg.Window('Part Color setup', self.layout)

        while self.setting:
            event, values = window.read()

            if event == sg.WIN_CLOSED:
                break
            elif event == 'start':
                proceed = False
                process = Process(proceed)

                while not proceed:
                    proceed = process.run()

    def result():
        pass