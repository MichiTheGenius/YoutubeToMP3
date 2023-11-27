import os
from pytube import Playlist


def get_path_from_file():
    # open the path file and assign a path variable the content of that file
    path = ""
    with open("path.txt", "r") as path_file:
        path = path_file.read()
    return path


def get_playlist_urls(url):
    # make an array with all video urls in the playlist with the help of pytube
    playlist = Playlist(url)

    video_urls = playlist.video_urls

    return video_urls


def compare_vid_vs_playlist(url):
    if "playlist" in url:
        return "playlist"
    elif "watch" in url:
        return "video"
    return "invalid"


def path_file_exists():
    return os.path.isfile("path.txt")


def write_path_to_file(path):
    with open("path.txt", "w") as path_file:
        path_file.write(path)


def change_path():
    new_path = ""
    if path_file_exists():
        current_path = get_path_from_file()
        new_path = input(
            f"Enter a new download path (The current one is {current_path}): ")
    else:
        new_path = input(f"Enter a new download path: ")

    # if the inputted path is empty we don't write it to the file
    if new_path == current_path:
        print(f"download path is already set to {current_path}!")
    elif new_path != "":
        write_path_to_file(new_path)
        print(f"changed download path to {new_path}!")
    else:
        print("download path is empty!")

def list_path():
    if path_file_exists():
        current_path = get_path_from_file()
        print(f"The current path is {current_path}")
    else:
        print(
            "You don't have a path file yet! Create one by entering c in the url field.")


def filter_out_correct_video(video):
    # get correct video format -> this took a lot of trying around to fine tune
    return video.streams.filter(audio_codec="mp4a.40.2", mime_type="audio/mp4").first()


def get_mp4_file(path, correct_video):
    # remove the single and double quotes from the song name as it causes errors
    default_filename = correct_video.default_filename.replace(
        '\'', '').replace('"', '')

    # if the path from the user doesn't have a "/" at the end we need to add it
    if not path.endswith("/"):
        return f"{path}/{default_filename}"
    else:
        return f"{path}{default_filename}"


def get_mp3_file(path, title, channel_name):
    # remove the single and double quotes from the song name as it causes errors
    video_title = title.replace('\'', '').replace('"', '')
    # default_filename = correct_video.default_filename.replace(
    #    ".mp4", ".mp3").replace("'", "").replace('"', '')

    channel_name = channel_name.replace(
        '\'', '').replace('"', '').replace('?', '')

    # if the path from the user doesn't have a "/" at the end we need to add it
    if not path.endswith("/"):
        return f"{path}/{video_title} - {channel_name}.mp3"
    else:
        return f"{path}{video_title} - {channel_name}.mp3"


def convert_mp4_to_mp3(mp4_file, mp3_file):
    # command to convert mp4 to mp3 with ffmpeg. -i for input, -f for filetype, -ab for bitrate, -vn for no video
    convert_command = f"ffmpeg -loglevel quiet -i '{
        mp4_file}' -f mp3 -ab 192000 -vn '{mp3_file}'"

    # execute the convert command
    os.system(convert_command)


def add_mp3_metadata(mp3_file, title, channel_name, album_name, year, ask_for_album_and_date):
    song_title = title.replace('\'', '').replace('"', '')

    artist_remove_tags = ['\'', '"', ' - Topic', 'Official ', ' Official']
    for tag in artist_remove_tags:
        artist = channel_name.replace(tag, '')

    if ask_for_album_and_date:
        command = f"id3v2 --artist '{artist}' --song '{
            song_title}' --album '{album_name}' --year {year} '{mp3_file}'"
    else:
        command = f"id3v2 --artist '{artist}' --song '{
            song_title}' '{mp3_file}'"

    os.system(command)

def print_help(ask_for_album_and_year):
    print("---Available commands---")
    print("q - quit the program")
    print("h - list this help message")
    print("c - change the download path of the music (e.g. /home/user/Music)")
    print("l - list the current path of the music")
    if ask_for_album_and_year:
        print("t - toggle whether you want to enter the album and year of the song (currently ON)")
    else:
        print("t - toggle whether you want to enter the album and year of the song (currently OFF)")