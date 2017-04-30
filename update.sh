#!/bin/bash

source .config
wget $CAMERA_URL -O image.jpg
python slack_delete.py
python slack_upload.py
