# YoutubeDownloaderPython

A program that converts a youtube link to a music mp3 file. It is written in python using the pytube module. It works best for Debian Linux systems because of the provided script that installs all the needed dependencies. But if you are able to make it work on Windows or other Linux Distributions go for it!

**USAGE**:
- clone the repo
- change into the newly acquired directory
- run the requirements.sh script in order to install all dependencies needed
- (You can look into it to check if you are ok with the things that will be installed)
    - ./requirements.sh
- if it does not work try making it executable with the command:
    - chmod +x ./requirements.sh
- open the path.txt file with your favorite text editor and enter your desired download path
    - example: /home/user/Music
- run the script with python3 
    - python3 yt_mp3.py
- Enter the url of your desired youtube video
- Look inside your entered donwload path to find your tunes