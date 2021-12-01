import pytube
import os

black = "\u001b[30m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
magenta = "\u001b[35m"
cyan = "\u001b[36m"
white = "\u001b[37m"
reset = "\u001b[0m"


def reset_color():
    print(reset)


def print_blue_text(text):
    print(f'{blue}{text}', end="")
    reset_color()


def filter_out_correct_video(video):
    return video.streams.filter(
        audio_codec="mp4a.40.2", mime_type="audio/mp4").first()


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


def main():
    while True:
        url = input(
            "Enter url(or q to quit, c to change the path, l to list the path): ")
        if url.lower() == 'q':
            break
        elif url.lower() == 'c':
            current_path = get_path_from_file()
            new_path = input(
                f"Enter a new download path (The current one is {current_path}): ")
            if new_path != "":
                write_path_to_file(new_path)
            continue
        elif url.lower() == 'l':
            current_path = get_path_from_file()
            print(f"The current path is {current_path}")
            continue

        pytube_video = pytube.YouTube(url)

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
        print_blue_text(f"Find your tunes in the folder {download_path}!")


if __name__ == "__main__":
    main()
