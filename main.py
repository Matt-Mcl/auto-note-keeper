import os
import sys
import gkeepapi
import requests
import subprocess
from dotenv import load_dotenv

load_dotenv()

def main():
    keep = gkeepapi.Keep()
    email = os.getenv('EMAIL')
    secret = os.getenv('SECRET')
    keep.login(email, secret)

    note = keep.find(query='Raspberry Pi Auto Note')
    try:
        next(note).delete()
    except StopIteration:
        # Note doesn't exist
        pass

    ip = requests.get('https://ifconfig.me/')
    temp_command = ["cat", "/sys/class/thermal/thermal_zone0/temp"]
    process = subprocess.Popen(temp_command, stdout=subprocess.PIPE)
    output, error = process.communicate()

    output = int(output.decode('ascii')[:-1])/1000

    note = keep.createNote('Raspberry Pi Auto Note', f"IP: {ip.text}\nTemperature: {output}°C")#
    note.color = gkeepapi.node.ColorValue.Yellow

    keep.sync()
    


if __name__ == '__main__':
    main()
    print('Ran successfully')
    sys.stdout.flush()
    sys.stderr.flush()
