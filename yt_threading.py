import pytube
import os
from pytube import Playlist
import numpy as np
from threading import Thread
import colors
import utils


class Converter:
    def __init__(self):
        self.main()

    def get_playlist_urls(self, url):
        # make an array with all video urls in the playlist with the help of pytube
        playlist = Playlist(url)

        video_urls = playlist.video_urls

        return video_urls

    def thread_main(self, start, end):
        # end + 1 because the loop leaves out the last number i.e if the end is 30 it ends at 29
        for i in range(start, end + 1):
            # make a video out of the current url in the loop that pytube can use
            pytube_video = pytube.YouTube(self.playlist_urls[i])
            channel_url = pytube_video.channel_url
            channel_name = pytube.Channel(channel_url).channel_name

            # get the current download path from the text file
            download_path = utils.get_path_from_file()
            colors.print_blue_text(f"video is downloading to {download_path}!")

            # i + 1 because the loop starts at 0 but youtube starts at 1
            colors.print_yellow_text(
                f"You are currently at video {i+1} of {self.end_index}")

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

    def main(self):
        while True:
            playlist_url_input = input(
                "Enter playlist url(or q to quit, c to change the path, l to list the path): ")
            if playlist_url_input.lower() == 'q':
                quit()
            elif playlist_url_input.lower() == 'c':
                utils.change_path()
                continue  # jump to start of while loop -> ask the user again what he wants to do
            elif playlist_url_input.lower() == 'l':
                utils.list_path()
                continue
            else:
                break

        self.playlist_urls = self.get_playlist_urls(playlist_url_input)

        amount_of_videos = len(self.playlist_urls)
        print(f"You have {amount_of_videos} videos in your playlist")
        # first video should be 1 in youtube -> first element in array is 0 -> -1 solves the problem
        start_index = int(
            input("Enter the start index(The first video is always 1): ")) - 1

        # youtubes last video is e.g. 10 -> loop ends at 9 -> array ends at 9 -> perfect
        self.end_index = int(
            input(f"Enter the end index(the maximum is {amount_of_videos}): "))

        my_indices = [i for i in range(start_index, self.end_index)]

        thread_amount = int(input('Enter how many threads you want: '))

        my_index_split = np.array_split(my_indices, thread_amount)

        for arr in my_index_split:
            start = arr[0]
            end = arr[-1]
            print(f'{start}-{end}')
            my_thread = Thread(target=self.thread_main, args=(start, end, ))
            my_thread.start()


Converter()
