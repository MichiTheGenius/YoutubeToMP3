# YoutubeToMP3

A program that converts a youtube link to a music mp3 file. It is written in python using the pytube module. It works best for Debian and Arch Linux systems because of the provided scripts that install all the needed dependencies. But if you are able to make it work on Windows or other Linux Distributions then go for it!

## Important
If downloading a **playlist** from Youtube it **MUST** either be *public* or *unlisted* for it to work

## Usage
1. clone the repo by entering this command

	```sh
	git clone https://github.com/MichiTheGenius/YoutubeToMP3
	```

2. change into the newly acquired directory
	

	```sh
	cd YoutubeToMP3
	```

3. run the requirements.sh script in order to install all dependencies needed (You can look into it to check if you are ok with the things that will be installed)

	- if you are on a debian linux based system run:
	```sh
	reqs/requirements_deb.sh
	```

	- if you are on an arch linux based system run:
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
    
5. run one of the following scripts: 
	- this script recognizes whether it is a playlist or single video you want to download:
	```sh
	python3 yt_mp3.py
	```

	- for the playlist with multithreading run:
	- (note: this is an experimental feature and rather a proof of concept)
	```sh
	python3 yt_threading.py
	```

   
6. change the download path of your music -> enter c in the url field end enter a valid filepath

7. follow the programs intructions

## Help
- the indices asked from the playlist asked are the small numbers on the left of a playlist video

- simply choose the start and end video end everything in between will be downloaded
