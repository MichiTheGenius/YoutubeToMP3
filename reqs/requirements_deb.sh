#!/bin/sh

set -xe

sudo apt update
sudo apt install python python3 python3-pip ffmpeg
pip3 install pytube numpy
