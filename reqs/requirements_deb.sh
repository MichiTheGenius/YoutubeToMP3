#!/usr/bin/bash

set -xe

sudo apt update
sudo apt install python3 python3-pip ffmpeg
pip3 install pytube numpy
