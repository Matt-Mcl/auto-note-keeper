import os
import pytz
import gkeepapi
import requests
import subprocess
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def main():
    now = datetime.now(pytz.timezone("Europe/London")).strftime("%d/%m/%Y, %H:%M")
    keep = gkeepapi.Keep()
    email = os.getenv('EMAIL')
    secret = os.getenv('SECRET')
    keep.login(email, secret)

    # Get IP address
    ip = requests.get('https://ifconfig.me/')

    # Get and format temperature
    temp_command = ["cat", "/sys/class/thermal/thermal_zone0/temp"]
    process = subprocess.Popen(temp_command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    temperature = int(output.decode('ascii')[:-1])/1000

    # Create the text for the note
    note_text = f"Time: {now} \nIP: {ip.text} \nTemperature: {temperature}°C"

    #Update note, or create new
    try:
        note = next(keep.find(query='Raspberry Pi Auto Note'))
        note.text = note_text
    except StopIteration:
        note = keep.createNote('Raspberry Pi Auto Note', note_text)
        note.color = gkeepapi.node.ColorValue.Yellow
        note.pinned = True
    
    print(note)

    keep.sync()


if __name__ == '__main__':
    try:
        main()
        print('Ran successfully')
    except Exception as e:
        print(e)
        print('Run Failed')
