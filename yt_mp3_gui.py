from time import sleep
import pytube
import os
from gui import my_gui
import colors
import utils


class Converter(my_gui):
    def __init__(self):
        super().__init__("YoutubeToMP3", self.download_video)

    def download_video(self):
        link = super().get_link()
        # make a video out of the current url in the loop that pytube can use
        pytube_video = pytube.YouTube(link)
        channel_url = pytube_video.channel_url
        channel_name = pytube.Channel(channel_url).channel_name

        download_path = super().get_path_from_file()
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
