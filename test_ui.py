import PySimpleGUI as sg
from os.path import exists
from time import sleep

fileName = './yt-mp3-save-path.txt'

def __changeLine(line, string):
    if not exists(fileName):
        with open(fileName, 'w') as f:
            f.write('')
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()
    with open(fileName, 'w') as f:
        if (line < len(lines)):
            lines[line] = string
        else:
            lines.append(string)
        f.writelines('\n'.join(lines))

# saves the last used fetch path
def setFetchPath(path):
    path = path[:path.rfind('/') + 1]
    __changeLine(0, path)

# gets the last used fetch path
def getFetchPath():
    if exists(fileName):
        with open(fileName, 'r') as f:
            lines = f.readlines()
            if len(lines) > 0:
                return lines[0].rstrip()
    return '~/'

# switches pages
def switchPage(key):
    for page in pages:
        if page == key:
            window[page].update(visible=True)
        else:
            window[page].update(visible=False)


sg.theme('DarkGray5')

pages = ['home', 'progress']

page0 = [   [sg.Text('Enter Link')],
            [sg.Input(key='-link-', expand_x=True)],
            [sg.Text('Choose export location')],
            [sg.Input(key='-path-', expand_x=True), sg.FolderBrowse('Browse', initial_folder=getFetchPath())],
            [sg.Text('Convert to mp3')],
            [sg.Button('Convert')] ]

page1 = [   [sg.Text('Converting: [0%]', key='-status-')],
            [sg.ProgressBar(max_value=100, key='-progress-', orientation='horizontal', size=(20, 5))],
            [sg.Text('')] ]

layout = [ [sg.Column(page0, key=pages[0]),
            sg.Column(page1, key=pages[1], visible=False)] ]

window = sg.Window('YoutubeToMP3', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Convert':
        switchPage('progress')
        for i in range(100):
            window['-progress-'].update(current_count=i + 1)
            window['-status-'].update(value='Converting: [' + str(i + 1) +'%]')
            print(i)
            sleep(0.02)

        sg.popup('Finished succesfully!', title='Succesful')
        switchPage('home')

window.close()