import os
from pytube import Playlist

# the tags that Youtube adds to the channel name that are removed
artist_remove_tags = [' - Topic', 'Official ', ' Official', 'Official', 'VEVO']


def get_path_from_file():
    # open the path file and assign a path variable the content of that file
    path = ""
    with open("path.txt", "r") as path_file:
        path = path_file.read()
    return path


def get_playlist_urls(url):
    """
    return the array of urls from a Youtube playlist
    """
    # make an array with all video urls in the playlist with the help of pytube
    playlist = Playlist(url)
    return playlist.video_urls


def compare_vid_vs_playlist(url):
    """
    check whether the url leads to a video or playlist
    example :
        video   : https://music.youtube.com/watch?v=hTWKbfoikeg&list=OLAK5uy_lYnxawfGdkGePjdFhIYaS6LjP-Md6UYf0
        playlist: https://music.youtube.com/playlist?list=OLAK5uy_lYnxawfGdkGePjdFhIYaS6LjP-Md6UYf0
    """
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
    current_path = ""
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
    """
    get correct video format from Youtube -> m4a
    """
    return video.streams.filter(audio_codec="mp4a.40.2", mime_type="audio/mp4").first()


def get_mp4_file(path, correct_video):
    """
    combine the download path and default filename into one string
    used for converting with ffmpeg and deleting after conversion
    """
    # if the path from the user doesn't have a trailing slash '/' at the end, it needs to be added
    if not path.endswith("/"):
        return f"{path}/{correct_video.default_filename}"
    else:
        return f"{path}{correct_video.default_filename}"


def get_artist_from_channel_name(channel_name):
    """
    remove tags like "VEVO", "Official" from the artist's name that Youtube adds to the channel name
    """
    for tag in artist_remove_tags:
        channel_name = channel_name.replace(tag, '')
    return channel_name


def get_mp3_file(path, title, channel_name):
    """
    replace the .mp4 extension in the filename with .mp3
    format the filename to: <song_title> - <artist>.mp3
    """
    # remove the single and double quotes from the song name as it causes errors with many filesystems
    # song_title = title.replace('\'', '').replace('"', '')

    artist = get_artist_from_channel_name(channel_name)
    # if the path from the user doesn't have a trailing slash '/' at the end, it needs to be added
    if not path.endswith("/"):
        return f"{path}/{title} - {artist}.mp3"
    else:
        return f"{path}{title} - {artist}.mp3"


def convert_mp4_to_mp3(mp4_file, mp3_file):
    """
    convert mp4 to mp3 with ffmpeg. -i for input, -f for filetype, -ab for bitrate, -vn for no video
    """
    convert_command = f"ffmpeg -loglevel quiet -i \"{
        mp4_file}\" -f mp3 -ab 192000 -vn \"{mp3_file}\""
    #print(f"convert command: {convert_command}")

    # execute the convert command
    os.system(convert_command)


def add_mp3_metadata(mp3_file, title, channel_name, album_name, year, ask_for_album_and_date):
    song_title = title
    artist = get_artist_from_channel_name(channel_name)
    # add the mp3 metadata with the 'id3v2' command line program
    if ask_for_album_and_date:
        command = f"id3v2 --artist \"{artist}\" --song \"{
            song_title}\" --album \"{album_name}\" --year {year} \"{mp3_file}\""
    else:
        command = f"id3v2 --artist \"{artist}\" --song \"{
            song_title}\" \"{mp3_file}\""

    #print(f"metadata command: {command}")

    os.system(command)


def print_help(ask_for_album_and_year):
    print("")
    print("A command line program to download music from Youtube")
    print("")
    print("---Available commands---")
    print("q - quit the program")
    print("h - list this help message")
    print("c - change the download path of the music (e.g. /home/user/Music)")
    print("l - list the current path of the music")
    if ask_for_album_and_year:
        print("a - toggle whether you want to enter the album and year of the song (currently ON)")
    else:
        print("a - toggle whether you want to enter the album and year of the song (currently OFF)")
    print("")
