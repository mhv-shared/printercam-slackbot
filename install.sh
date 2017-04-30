#!/bin/bash

echo "*/5 * * * * cd $PWD && ./update.sh" > crontab
crontab -l -u $USER | cat - crontab | crontab -u $USER -

