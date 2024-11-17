#!/usr/bin/env python3
import pytubefix
import os
import colors
import utils


def download_single_video(download_path, url, ask_for_album_and_year):
    # ask the user for the album and year of the song
    if ask_for_album_and_year:
        album_name = input("Enter the name of the album the song belongs to: ")
        year = input("Enter the year the song was released in: ")
    else:
        album_name = ''
        year = 0
    colors.print_blue_text(f"Video is downloading to {download_path}...")

    # make a video out of the current url that pytube can use
    pytube_video = pytubefix.YouTube(url)
    channel_name = pytubefix.Channel(pytube_video.channel_url).channel_name

    # get the audio file out of all the options
    correct_video = utils.filter_out_correct_video(pytube_video)
    title = correct_video.title

    # download that file
    correct_video.download(download_path)
    colors.print_blue_text("Finished downloading!")
    colors.print_blue_text("Converting to mp3...")

    # input filename for ffmpeg (combine the download path with the title of the video)
    mp4_file = utils.get_mp4_file(download_path, correct_video)
    mp3_file = utils.get_mp3_file(
        download_path, title, channel_name)

    # use ffmpeg to convert the downloaded mp4 to an mp3
    utils.convert_mp4_to_mp3(mp4_file, mp3_file)

    # delete the remaining mp4 file
    os.remove(mp4_file)

    # add the mp3 metadata: song title, artist, (if the ask_for_album_and_year flag is set) album, year
    utils.add_mp3_metadata(mp3_file, title, channel_name,
                           album_name, year, ask_for_album_and_year)

    colors.print_yellow_text("Finished converting!")


def download_playlist(download_path, url, ask_for_album_and_year):
    playlist_urls = utils.get_playlist_urls(url)
    amount_of_videos = len(playlist_urls)
    print(f"There are {amount_of_videos} videos in the playlist.")

    # first video in youtube has index 1 -> first element in array has index 0 -> -1 solves the problem
    start_index = int(
        input("Enter the start index (The first video is always 1): ")) - 1

    # youtubes last video is e.g. 10 -> loop ends at 9 -> array ends at 9 -> perfect
    end_index = int(
        input(f"Enter the end index (the maximum is {amount_of_videos}): "))

    for i in range(start_index, end_index):
        # i + 1 because the loop starts at 0 but youtube starts at 1
        colors.print_yellow_text(f"Currently at video {i+1} of {end_index}...")
        download_single_video(
            download_path, playlist_urls[i], ask_for_album_and_year)


def run():
    if not utils.path_file_exists():
        print("You don't have a path file yet! Create one by entering c in the url field.")
    ask_for_album_and_year = False
    utils.print_help(ask_for_album_and_year)
    while 1:
        url = input("Enter a YouTube URL or a command from above: ")
        if url.lower() == 'q':
            quit()  # quit the loop -> program finishes
        elif url.lower() == 'h':
            utils.print_help(ask_for_album_and_year)
            continue
        elif url.lower() == 'c':
            utils.change_path()
            continue  # jump to start of while loop -> ask the user again what he wants to do
        elif url.lower() == 'l':
            utils.list_path()
            continue
        elif url.lower() == 'a':
            ask_for_album_and_year = not ask_for_album_and_year
            if ask_for_album_and_year:
                print("Enabled the ask_for_album_and_year flag.")
                print("After entering an url you will be prompted to enter the name of the album, as well as the year the song was released in.")
            else:
                print("disabled the ask_for_album_and_year flag!")
            continue

        url_kind = utils.compare_vid_vs_playlist(url)
        download_path = utils.get_path_from_file()

        if url_kind == "video":
            download_single_video(
                download_path, url, ask_for_album_and_year)
        elif url_kind == "playlist":
            download_playlist(
                download_path, url, ask_for_album_and_year)

        colors.print_red_text(
            f"Finished downloading all of your songs! Find your files in the folder {download_path}!")


if __name__ == '__main__':
    run()
