import os


def get_path_from_file():
    # open the path file and assign a path variable the content of that file
    path = ""
    with open("path.txt", "r") as path_file:
        path = path_file.read()
    return path


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
    if new_path != "":
        write_path_to_file(new_path)


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
    # replace the single and double quotes with nothing from the song name as it causes errors
    default_filename = correct_video.default_filename.replace(
        "'", "").replace('"', '')

    # if the path from the user doesn't have a "/" at the end we need to add it
    if not path.endswith("/"):
        return f"{path}/{default_filename}"
    else:
        return f"{path}{default_filename}"


def get_mp3_file(path, correct_video, channel_name):
    # replace the single and double quotes with nothing from the song name as it causes errors
    default_filename = correct_video.default_filename.replace(
        ".mp4", ".mp3").replace("'", "").replace('"', '')
    channel_name = channel_name.replace("'", "").replace('"', '')
    # if the path from the user doesn't have a "/" at the end we need to add it
    if not path.endswith("/"):
        return f"{path}/{channel_name} - {default_filename}"
    else:
        return f"{path}{channel_name} - {default_filename}"


def convert_mp4_to_mp3(mp4_file, mp3_file):
    # command to convert mp4 to mp3 with ffmpeg. -i for input, -f for filetype, -ab for bitrate, -vn for no video
    convert_command = f"ffmpeg -loglevel quiet -i '{mp4_file}' -f mp3 -ab 192000 -vn '{mp3_file}'"

    # execute the convert command
    os.system(convert_command)
