import PySimpleGUI as sg
from time import sleep
from utils import check_path_is_valid, get_path_from_file, path_file_exists, write_path_to_file, compareVidVSPlaylist
from yt_mp3 import Converter

# saves the last used fetch path
def setSavePath(path):
    write_path_to_file(path)

# gets the last used fetch path
def getSavePath():
    if path_file_exists():
        return get_path_from_file()
    return '~/'

# checks if video is playlist or video
def checkVideoType(url):
    return compareVidVSPlaylist(url)

# switches pages
def switchPage(key):
    for page in pages:
        if page == key:
            window[page].update(visible=True)
        else:
            window[page].update(visible=False)




sg.theme('DarkGray5')

pages = ['home']

# home
page0 = [   [sg.Text('Enter Link')],
            [sg.Input(key='-link-', expand_x=True)],
            [sg.Text('Choose export location')],
            [sg.Input(getSavePath(), key='-path-', expand_x=True), sg.FolderBrowse('Browse', initial_folder=getSavePath())],
            [sg.Text('Convert to mp3')],
            [sg.Button('Convert')] ]

layout = [ [sg.Column(page0, key=pages[0])] ]

window = sg.Window('YoutubeToMP3', layout)

converter = Converter(True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Convert':
        url = values['-link-']
        savePath = values['-path-']
        videoType = checkVideoType(url)
        if (videoType != 'invalid'):
            if (check_path_is_valid(savePath)):
                setSavePath(savePath)
                try:
                    converter.download_gui(url, True)
                except:
                    sg.popup('The specified url is invalid', title='Error')
                sg.popup('Video(s) have been succesfully converted', title='Finished')
            else:
                sg.popup('The specified path does not exist', title='Error')
        else:
            sg.popup('The specified url is invalid', title='Error')

window.close()