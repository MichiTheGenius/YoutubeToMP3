# YoutubeToMP3Python

A program that converts a youtube link to a music mp3 file. It is written in python using the pytube module. It works best for Debian and Arch Linux systems because of the provided script that installs all the needed dependencies. But if you are able to make it work on Windows or other Linux Distributions then go for it!

## Usage
1. open a terminal window (the key-combination ctrl-alt-t opens a terminal in most linux distributions)
2. clone the repo by entering this command

	```sh
	git clone https://github.com/MichiTheGenius/YoutubeToMP3Python
	```

2. change into the newly acquired directory
	

	```sh
	cd YoutubeToMp3Python
	```

3. run the requirements.sh script in order to install all dependencies needed (You can look into it to check if you are ok with the things that will be installed)

	- if you are on a debian linux system run:
	```sh
	reqs/requirements_deb.sh
	```

	- if you are on an arch linux system run:
	```sh
	reqs/requirements_arch.sh
	```

4. (optional) if it does not work try making it executable with the command:

    - if you are on a debian linux system run:
	```sh
	chmod +x reqs/requirements_deb.sh
	```

	- if you are on an arch linux system run:
	```sh
	chmod +x reqs/requirements_arch.sh
	```

5. choose whether you want to download a single video or videos from a playist

	- for for the single video run:
	```sh
	python3 yt_mp3.py
	```

	- for the playlist run:
	```sh
	python3 yt_playlist_mp3.py
	```

	- for the playlist with multithreading run:
	```sh
	python3 yt_threading.py
	```

6. change the download path of your music -> enter c in the url field end enter a valid filepath

7. follow the programs intructions

### Help
- the indices asked from the playlist asked are the small numbers on the left of a playlist video

- simply choose the start and end video end everything in between will be downloaded
