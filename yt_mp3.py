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
    print(f'{blue}{text}')
    reset_color()


def main():
    url = input("Enter url: ")
    my_video = pytube.YouTube(url)

    # get the audio file out of all the options
    finished_video = my_video.streams.filter(
        audio_codec="mp4a.40.2", mime_type="audio/mp4").first()

    print_blue_text("Video is downloading!")
    # download that file
    finished_video.download("Music/")
    print_blue_text("finished downloading!")

    print_blue_text("Converting to mp3")

    # input filename for ffmpeg
    mp4_file = f"Music/{finished_video.default_filename}"

    # output mp3 file (replace the default .mp4 in the filename with .mp3)
    mp3_output = f"Music/{finished_video.default_filename.replace('.mp4', '.mp3')}"

    # command to convert mp4 to mp3 with ffmpeg. -i for input, -f for filetype, -ab for bitrate, -vn for no video
    convert_command = f"ffmpeg -i '{mp4_file}' -f mp3 -ab 192000 -vn '{mp3_output}'"

    # execute the convert command
    os.system(convert_command)

    # delete the remaining mp4 file we don't need anymore
    os.remove(mp4_file)

    print_blue_text("finished converting!")


if __name__ == "__main__":
    main()
