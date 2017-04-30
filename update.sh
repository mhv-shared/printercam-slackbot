#!/bin/bash

source .secrets
wget http://admin:@dcs-932lb1_09ae55.local/image.jpg -O image.jpg
python slack_delete.py
python slack_upload.py
