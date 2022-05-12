from os import getenv
from pytz import timezone
from requests import put, get
from subprocess import check_output
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

key = getenv('KEY')
token = getenv('TOKEN')
cards = getenv('CARDS').split(',')

# Get time
now = datetime.now(timezone("Europe/London")).strftime("%d/%m/%Y, %H:%M")

# Get IP address
ip = get('https://ifconfig.me/')

# Get and format temperature
temp_command = ["cat", "/sys/class/thermal/thermal_zone0/temp"]
output = check_output(temp_command)
temperature = int(output.decode('ascii')[:-1])/1000

notes = [
    (f"Time: {now}", ""),
    ("IP: (Hidden)", ip.text),
    (f"Temperature: {temperature}°C", "")
]

for note, card_id in zip(notes, cards):
    put(
        url = f"https://api.trello.com/1/cards/{card_id}", 
        params = {
            "key": key,
            "token": token,
            "name": note[0],
            "desc": note[1]
        }
    )
