import pytube
import os
from pytube import Playlist

black = "\u001b[30m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
magenta = "\u001b[35m"
cyan = "\u001b[36m"
white = "\u001b[37m"
reset = "\u001b[0m"

def get_playlist_urls(url):
    playlist = Playlist(url)

    video_urls = playlist.video_urls

    return video_urls

def reset_color():
    print(reset)


def print_blue_text(text):
    print(f'{blue}{text}', end="")
    reset_color()

def print_red_text(text):
    print(f'{red}{text}', end="")
    reset_color()

def filter_out_correct_video(video):
    return video.streams.filter(audio_codec="mp4a.40.2", mime_type="audio/mp4").first()


def get_mp4_file(path, correct_video):
    if not path.endswith("/"):
        return f"{path}/{correct_video.default_filename}"
    else:
        return f"{path}{correct_video.default_filename}"


def get_path_from_file():
    path = ""
    with open("path.txt", "r") as path_file:
        path = path_file.read()
    return path


def write_path_to_file(path):
    with open("path.txt", "w") as path_file:
        path_file.write(path)


def change_path():
    current_path = get_path_from_file()
    new_path = input(f"Enter a new download path (The current one is {current_path}): ")
    if new_path != "":
        write_path_to_file(new_path)


def list_path():
    current_path = get_path_from_file()
    print(f"The current path is {current_path}")


def main():
    while True:
        playlist_url_input = input("Enter playlist url(or q to quit, c to change the path, l to list the path): ")
        if playlist_url_input.lower() == 'q':
            quit()
        elif playlist_url_input.lower() == 'c':
            change_path()
            continue 
        elif playlist_url_input.lower() == 'l':
            list_path()
            continue
        else:
            break

    playlist_urls = get_playlist_urls(playlist_url_input)

    start_index = int(input("Enter start index: ")) - 1
    end_index = int(input("Enter end index: ")) - 1

    for i in range(start_index, end_index+1):
        pytube_video = pytube.YouTube(playlist_urls[i])

        download_path = get_path_from_file()
        print_blue_text(f"video is downloading to {download_path}!")

        # get the audio file out of all the options
        correct_video = filter_out_correct_video(pytube_video)

        # download that file
        correct_video.download(download_path)
        print_blue_text("finished downloading!")

        print_blue_text("converting to mp3!")

        # input filename for ffmpeg
        mp4_file = get_mp4_file(download_path, correct_video)

        # output mp3 file (replace the default .mp4 in the filename with .mp3)
        mp3_output = mp4_file.replace(".mp4", ".mp3")

        # command to convert mp4 to mp3 with ffmpeg. -i for input, -f for filetype, -ab for bitrate, -vn for no video
        convert_command = f"ffmpeg -i '{mp4_file}' -f mp3 -ab 192000 -vn '{mp3_output}'"

        # execute the convert command
        os.system(convert_command)

        # delete the remaining mp4 file we don't need anymore
        os.remove(mp4_file)

        print_blue_text("finished converting!")
    print_red_text(f"Finished downloading all of your videos! Find your tunes in the folder {download_path}!")


if __name__ == "__main__":
    main()
