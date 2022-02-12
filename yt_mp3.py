import pytube
import os

# ansi color codes to print out colored text in the terminal
black = "\u001b[30m"
red = "\u001b[31m"
green = "\u001b[32m"
yellow = "\u001b[33m"
blue = "\u001b[34m"
magenta = "\u001b[35m"
cyan = "\u001b[36m"
white = "\u001b[37m"
reset = "\u001b[0m"


class Converter():
    def __init__(self):
        if not self.path_file_exists():
            print(
                "You don't have a path file yet! Create one by entering c in the url field.")
        self.download_video()

    def download_video(self):
        while 1:
            url = input(
                "Enter url(or q to quit, c to change the path, l to list the path): ")
            if url.lower() == 'q':
                break  # quit the loop -> program finishes
            elif url.lower() == 'c':
                self.change_path()
                continue  # jump to start of while loop -> ask the user again what he wants to do
            elif url.lower() == 'l':
                self.list_path()
                continue

            # make a video out of the current url in the loop that pytube can use
            pytube_video = pytube.YouTube(url)
            channel_url = pytube_video.channel_url
            channel_name = pytube.Channel(channel_url).channel_name

            download_path = self.get_path_from_file()
            self.print_blue_text(f"video is downloading to {download_path}!")

            # get the audio file out of all the options
            correct_video = self.filter_out_correct_video(pytube_video)

            # download that file
            correct_video.download(download_path)
            self.print_blue_text("finished downloading!")
            self.print_blue_text("converting to mp3!")

            # input filename for ffmpeg
            mp4_file = self.get_mp4_file(download_path, correct_video)

            # output mp3 file (replace the default .mp4 in the filename with .mp3)
            mp3_file = self.get_mp3_file(
                download_path, correct_video, channel_name)

            self.convert_mp4_to_mp3(mp4_file, mp3_file)

            # delete the remaining mp4 file we don't need anymore
            os.remove(mp4_file)

            self.print_blue_text("finished converting!")

    def reset_color(self):
        print(reset)

    def print_blue_text(self, text):
        print(f'{blue}{text}', end="")
        self.reset_color()

    def print_red_text(self, text):
        print(f'{red}{text}', end="")
        self.reset_color()

    def filter_out_correct_video(self, video):
        # get correct video format -> this took a lot of trying around to fine tune
        return video.streams.filter(audio_codec="mp4a.40.2", mime_type="audio/mp4").first()

    def get_mp4_file(self, path, correct_video):
        # replace the single and double quotes with nothing from the song name as it causes errors
        default_filename = correct_video.default_filename.replace(
            "'", "").replace('"', '')

        # if the path from the user doesn't have a "/" at the end we need to add it
        if not path.endswith("/"):
            return f"{path}/{default_filename}"
        else:
            return f"{path}{default_filename}"

    def get_mp3_file(self, path, correct_video, channel_name):
        # replace the single and double quotes with nothing from the song name as it causes errors
        default_filename = correct_video.default_filename.replace(
            ".mp4", ".mp3").replace("'", "").replace('"', '')
        channel_name = channel_name.replace("'", "").replace('"', '')
        # if the path from the user doesn't have a "/" at the end we need to add it
        if not path.endswith("/"):
            return f"{path}/{channel_name} - {default_filename}"
        else:
            return f"{path}{channel_name} - {default_filename}"

    def convert_mp4_to_mp3(self, mp4_file, mp3_file):
        # command to convert mp4 to mp3 with ffmpeg. -i for input, -f for filetype, -ab for bitrate, -vn for no video
        convert_command = f"ffmpeg -i '{mp4_file}' -f mp3 -ab 192000 -vn '{mp3_file}'"

        # execute the convert command
        os.system(convert_command)

    def get_path_from_file(self):
        # open the path file and assign a path variable the content of that file
        path = ""
        with open("path.txt", "r") as path_file:
            path = path_file.read()
        return path

    def path_file_exists(self):
        return os.path.isfile("path.txt")

    def write_path_to_file(self, path):
        with open("path.txt", "w") as path_file:
            path_file.write(path)

    def change_path(self):
        new_path = ""
        if self.path_file_exists():
            current_path = self.get_path_from_file()
            new_path = input(
                f"Enter a new download path (The current one is {current_path}): ")
        else:
            new_path = input(f"Enter a new download path: ")

        # if the inputted path is empty we don't write it to the file
        if new_path != "":
            self.write_path_to_file(new_path)

    def list_path(self):
        if self.path_file_exists():
            current_path = self.get_path_from_file()
            print(f"The current path is {current_path}")
        else:
            print(
                "You don't have a path file yet! Create one by entering c in the url field.")


if __name__ == '__main__':
    converter = Converter()
