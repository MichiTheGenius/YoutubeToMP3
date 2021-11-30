import pytube
import os


black = '\u001b[30m'
red = '\u001b[31m'
green = '\u001b[32m'
yellow = '\u001b[33m'
blue = '\u001b[34m'
magenta = '\u001b[35m'
cyan = '\u001b[36m'
white = '\u001b[37m'
reset = '\u001b[0m'


def printBlueText(text):
    print(f'{blue}{text}')


url = input('Enter url: ')
my_video = pytube.YouTube(url)
# videos = []
# video_resolutions = []
# for stream in my_video.streams.filter(audio_codec="mp4a.40.2", mime_type='audio/mp4'):
#     print(stream)
#     videos.append(stream)
#     video_resolutions.append(stream.resolution)

# i = 0
# for resolution in video_resolutions:
#     print(f'{i}. {resolution}')
#     i += 1

#choice = int(input('Enter desired resolution number: '))
finished_video = my_video.streams.filter(
    audio_codec="mp4a.40.2", mime_type='audio/mp4').first()  # videos[choice]
printBlueText('Video is downloading!')
finished_video.download('/home/michael/Downloads/Music')
printBlueText('finished downloading!')

printBlueText('Converting to mp3')
mp4_file = finished_video.default_filename
mp3_output = finished_video.default_filename.replace('.mp4', '.mp3')
convert_command = f'ffmpeg -i "{mp4_file}" -f mp3 -ab 192000 -vn "{mp3_output}"'
os.system(convert_command)
os.remove(mp4_file)
printBlueText('finished converting!')
