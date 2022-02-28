import os
import sys
import gkeepapi
import requests
import subprocess
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def main():
    keep = gkeepapi.Keep()
    email = os.getenv('EMAIL')
    secret = os.getenv('SECRET')
    keep.login(email, secret)
    # Find existing note
    note = keep.find(query='Raspberry Pi Auto Note')
    try:
        # Delete existing note
        next(note).delete()
    except StopIteration:
        # Note doesn't exist
        pass
    # Get IP address
    ip = requests.get('https://ifconfig.me/')
    # Get temperature
    temp_command = ["cat", "/sys/class/thermal/thermal_zone0/temp"]
    process = subprocess.Popen(temp_command, stdout=subprocess.PIPE)
    output, error = process.communicate()
    # Format temperature
    output = int(output.decode('ascii')[:-1])/1000
    now = datetime.now().strftime("%d/%m/%Y, %H:%M")
    # Create note
    note = keep.createNote('Raspberry Pi Auto Note', f"Time: {now} \nIP: {ip.text} \nTemperature: {output}°C")
    print(note)
    note.color = gkeepapi.node.ColorValue.Yellow

    keep.sync()


if __name__ == '__main__':
    main()
    print('Ran successfully')
    sys.stdout.flush()
    sys.stderr.flush()
