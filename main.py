import os
import pytz
import requests
import subprocess
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

key = os.getenv('KEY')
token = os.getenv('TOKEN')
cards = os.getenv('CARDS').split(',')

# Get time
now = datetime.now(pytz.timezone("Europe/London")).strftime("%d/%m/%Y, %H:%M")

# Get IP address
ip = requests.get('https://ifconfig.me/')

# Get and format temperature
temp_command = ["cat", "/sys/class/thermal/thermal_zone0/temp"]
output = subprocess.check_output(temp_command)
temperature = int(output.decode('ascii')[:-1])/1000

notes = [f"Time: {now}", f"IP: {ip.text}", f"Temperature: {temperature}°C"]

for note, card_id in zip(notes, cards):
    requests.put(
        url = f"https://api.trello.com/1/cards/{card_id}", 
        params = {
            "key": key,
            "token": token,
            "name": note
        }
    )
