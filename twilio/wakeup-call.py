#!/usr/bin/env python3

from twilio.rest import Client
import argparse
from secret import AUTH_TOKEN
from secret import ACCOUNT_SID
from secret import TWILIO_PHONE_NUMBER

# Your Twilio account SID and Auth Token
# ACCOUNT_SID = ''
# AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'

# Your Twilio phone number (must start with a '+' followed by the country code)
# TWILIO_PHONE_NUMBER = ''

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def make_wake_up_call(to, url):
    """
    Place a call to the given number and play an audio when the call is answered.

    :param to: The recipient phone number, e.g., '+19876543210'
    :param url: URL of the audio file (mp3 or wav) to be played
    """
    call = client.calls.create(
        to=to,
        from_=TWILIO_PHONE_NUMBER,
        url=url,
        method='GET'
    )
    print(f"Call to {to} initiated with SID: {call.sid}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make a wake-up call to a specified phone number with a specified audio.")
    parser.add_argument("recipient", help="Recipient's phone number in the format '+17870000000'.")
    parser.add_argument("audio_url", help="URL of the audio file to be played during the call.")
    args = parser.parse_args()

    make_wake_up_call(args.recipient, args.audio_url)
