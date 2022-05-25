#!/usr/bin/bash

set -xe

sudo pacman -S python3 python-pip ffmpeg
pip3 install pytube numpy
