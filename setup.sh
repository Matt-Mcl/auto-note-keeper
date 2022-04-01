#!/bin/bash

cron="*/5 * * * *" # Cron for every 5 minutes
directory="$(pwd)"
script="$directory/run.sh"
venvlocation="$directory/venv"
username=$(whoami)


if [ ! -d $venvlocation ]; then
    echo "venv not present - creating" 
    python3 -m venv venv
    source "venv/bin/activate"

    pip install --upgrade pip
    pip install -r requirements.txt
fi

bash run.sh "$directory"

# Delete existing crontabs - means crontab is only present once
crontab -r >> /dev/null

# Create crontab to run script
(crontab -l 2>/dev/null; echo "$cron $script $directory") | crontab -

echo "Created crontab for backups successfully:"
sudo crontab -u "$username" -l | grep "$script"
