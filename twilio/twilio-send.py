#!/usr/bin/env python3

import sys
import subprocess
from secret import AUTH_TOKEN
from secret import ACCOUNT_SID
from secret import TWILIO_PHONE_NUMBER

def send_message(phone_number, message):
    command = [
        'curl', 'https://api.twilio.com/2010-04-01/Accounts/{ACCOUNT_SID}/Messages.json', '-X', 'POST',
        '--data-urlencode', f'To=+{phone_number}',
        '--data-urlencode', 'From=+{TWILIO_PHONE_NUMBER}',
        '--data-urlencode', f'Body={message}\nMessage from WebNinja Corp.\nReply STOP to unsubscribe',
        '-u', f'{ACCOUNT_SID}:{AUTH_TOKEN}'
    ]

    subprocess.run(command)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./twilio-send.py <phone_number> <message>")
        sys.exit(1)

    phone_number = sys.argv[1]
    message = sys.argv[2]

    send_message(phone_number, message)
