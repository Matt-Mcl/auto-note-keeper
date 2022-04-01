# Auto Note Keeper

## What is this?

This is a small application that automatically logs data to a [Google Keep](https://www.google.com/keep/) note using a cronjob. This uses the the [gkeepapi PyPi package](https://pypi.org/project/gkeepapi/) to create and update notes.

## Setup

1. Create Google App Password here: https://myaccount.google.com/apppasswords

2. Create `.env` file with following contents:
```env
EMAIL=<GOOGLE_ACCOUNT_EMAIL>
SECRET=<GOOGLE_APP_PASSWORD>
```

3. Modify [main.py](main.py) to your liking. This example retrieves the date, public IP address and CPU temperatue of a Raspberry Pi 4: 

![note](https://user-images.githubusercontent.com/46825394/161248689-29ea5cbf-84b8-4b42-befd-466f9683d620.png)


4. Modify the cronjob in [setup.sh](setup.sh) to the interval you want. Default is 5 minutes.

5. Run [setup.sh](setup.sh)

## Notes

- This has only been tested on Ubuntu 20.04 but should work on and Unix system with Python and Bash.
