# YoutubeDownloaderPython

A program that converts a youtube link to a music mp3 file. It is written in python using the pytube module. It works best for Debian Linux systems because of the provided script that installs all the needed dependencies. But if you are able to make it work on Windows or other Linux Distributions go for it!

## Usage
- clone the repo
- change into the newly acquired directory
- run the requirements.sh script in order to install all dependencies needed
- (You can look into it to check if you are ok with the things that will be installed)
	
	- `./requirements.sh`
	
- if it does not work try making it executable with the command:
	
	- `chmod +x ./requirements.sh`

- choose whether you want to download a single video or videos from a playist
	- for the former run:
	
		- `python3 yt_mp3.py`

	- for the latter run:
	
		- `python3 yt_playlist_mp3.py`
	
- follow the programs intructions
- the indices asked from the playlist asked are the small numbers on the left of a playlist video
- simply choose the start and end video end everything in between will be downloaded
