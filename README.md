# YoutubeToMP3

A program that converts a youtube link to a music mp3 file. It is written in python using the pytube module. It works best for Debian and Arch Linux systems because of the provided scripts that install all the needed dependencies. But if you are able to make it work on Windows or other Linux Distributions then go for it!

## Important
- If downloading a **playlist** from Youtube it **MUST** either be *public* or *unlisted* for the program to work
- If you get any download related errors try to update the pytube library with the following command

	```sh
	pip3 install --upgrade --force-reinstall "git+https://github.com/pytube/pytube.git"
	```

## Usage
1. Clone the repo by entering this command

	```sh
	git clone https://github.com/MichiTheGenius/YoutubeToMP3
	```

2. Change into the newly acquired directory
	

	```sh
	cd YoutubeToMP3
	```

3. Follow the instructions in [INSTALL.md](./INSTALL.md) to install the needed dependencies.

4. Run one of the following scripts: 
	- this script recognizes whether it is a playlist or single video you want to download:
	```sh
	python3 yt_mp3.py
	```

	- for the playlist with multithreading run:
	- (note: this is an experimental feature and rather a proof of concept)
	```sh
	python3 yt_threading.py
	```

   
5. Change the download path of your music -> enter c in the url field end enter a valid filepath

6. Follow the programs intructions

## Help
- the indices asked from the playlist asked are the small numbers on the left of a playlist video

- simply choose the start and end video end everything in between will be downloaded
