#!/usr/bin/bash

set -xe

sudo apt update
sudo apt install python3 python3-pip ffmpeg
#pip3 install pytube numpy
pip3 install numpy
pip3 install git+https://github.com/baxterisme/pytube
