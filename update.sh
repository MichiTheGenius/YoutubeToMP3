#!/bin/bash

OS=$1

echo "updating YoutubeToMP3..."
if [ "$OS" = "ubuntu" ]; then
	sudo apt update
	sudo apt install ffmpeg python3 python3-pip
elif [ "$OS" = "fedora" ]; then
	sudo dnf update
	sudo dnf install ffmpeg-free python3 python3-pip
elif [ "$OS" = "arch" ]; then
	sudo pacman -Sy ffmpeg python3 python3-pip
else
	echo "unknown operating system: <$OS>! Try ./update.sh <ubuntu|fedora|arch>"
	exit
fi

git pull origin main
pip3 install numpy
pip3 install --upgrade --force-reinstall "git+https://github.com/pytube/pytube.git"
