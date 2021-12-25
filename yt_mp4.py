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


def reset_color():
    print(reset)


def print_blue_text(text):
    print(f'{blue}{text}', end="")
    reset_color()


def print_red_text(text):
    print(f'{red}{text}', end="")
    reset_color()




def get_final_filename(path, video, channel_name):
    default_filename = video.default_filename
    if not path.endswith("/"):
        return f"{path}/{channel_name} - {default_filename}"
    else:
        return f"{path}{channel_name} - {default_filename}"

def get_default_filename(path, video):
    default_filename = video.default_filename
    if not path.endswith("/"):
        return f"{path}/{default_filename}"
    else:
        return f"{path}{default_filename}"



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
        new_path = input(f"Enter a new download path (The current one is {current_path}): ")
    else:
        new_path = input(f"Enter a new download path: ")

        # if the inputted path is empty we don't write it ti the file
    if new_path != "":
        write_path_to_file(new_path)


def list_path():
    if path_file_exists():
        current_path = get_path_from_file()
        print(f"The current path is {current_path}")
    else:
        print("You don't have a path file yet! Create one by entering c in the url field.")


def main():
    while True:
        url = input("Enter url(or q to quit, c to change the path, l to list the path): ")
        if url.lower() == 'q':
            break  # quit the loop -> program finishes
        elif url.lower() == 'c':
            change_path()
            continue  # jump to start of while loop -> ask the user again what he wants to do
        elif url.lower() == 'l':
            list_path()
            continue

        # make a video out of the current url in the loop that pytube can use
        pytube_video = pytube.YouTube(url)

        vid_options = pytube_video.streams.filter(audio_codec="mp4a.40.2",mime_type="video/mp4")

        for i,vid in enumerate(vid_options):
            print(f'{i}. {vid}')

        user_option = int(input('Enter the option you want: '))

        channel_url = pytube_video.channel_url
        channel_name = pytube.Channel(channel_url).channel_name

        download_path = get_path_from_file()

        print_blue_text(f"video is downloading to {download_path}!")

        selected_video = vid_options[user_option]
        selected_video.download(download_path)

        default_filename = get_default_filename(download_path,selected_video)

        final_filename = get_final_filename(download_path,selected_video,channel_name)

        os.rename(default_filename,final_filename)

        print_red_text(f"Finished downloading all of your videos! Find your tunes in the folder {download_path}!")

if __name__ == "__main__":
    main()
