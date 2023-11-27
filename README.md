# YoutubeToMP3

![demo](./demo.png)

A program that converts a youtube link to a music mp3 file while adding useful metadata (name of artist, song title, year, album). It is written in python using the pytube module. It works best for Debian, Arch Linux and Fedora systems because of the provided instructions for installing all of the needed dependencies. But if you are able to make it work on Windows or other Linux Distributions then go for it!

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
	> this script recognizes whether it is a playlist or single video you want to download:
	> > ```sh>
	> > python3 yt_mp3.py
	> > ```
	> for the playlist with multithreading run:
	>
	> >```sh
	> >python3 yt_threading.py
	> >```
	> (note: this is an experimental feature and rather a proof of concept)
   
5. Change the download path of your music by entering `c` in the url field end providing a valid filepath (example: `/home/user/Music`)

6. The program automatically adds the artist's name as well as the song name to your mp3. Due to YouTube's limitations it is not able to fetch other data like the name of the album or the year the song was released. That is why the program implements a toggle that lets you chose whether you want to manually enter the album and year of the song. To use this toggle enter `t` in the url field

7. Follow the programs' intructions

## Help
- The indices asked from the playlist asked are the small numbers on the left of a playlist video

- Simply choose the start and end video end everything in between will be downloaded
