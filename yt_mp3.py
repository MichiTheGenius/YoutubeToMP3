import pytube
import os
import colors
import utils

class Converter():
    def __init__(self):
        if not utils.path_file_exists():
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
                utils.change_path()
                continue  # jump to start of while loop -> ask the user again what he wants to do
            elif url.lower() == 'l':
                utils.list_path()
                continue

            # make a video out of the current url in the loop that pytube can use
            pytube_video = pytube.YouTube(url)
            channel_url = pytube_video.channel_url
            channel_name = pytube.Channel(channel_url).channel_name

            download_path = utils.get_path_from_file()
            colors.print_blue_text(f"video is downloading to {download_path}!")

            # get the audio file out of all the options
            correct_video = utils.filter_out_correct_video(pytube_video)

            # download that file
            correct_video.download(download_path)
            colors.print_blue_text("finished downloading!")
            colors.print_blue_text("converting to mp3!")

            # input filename for ffmpeg
            mp4_file = utils.get_mp4_file(download_path, correct_video)

            # output mp3 file (replace the default .mp4 in the filename with .mp3)
            mp3_file = utils.get_mp3_file(
                download_path, correct_video, channel_name)

            utils.convert_mp4_to_mp3(mp4_file, mp3_file)

            # delete the remaining mp4 file we don't need anymore
            os.remove(mp4_file)

            colors.print_blue_text("finished converting!")

if __name__ == '__main__':
    converter = Converter()
