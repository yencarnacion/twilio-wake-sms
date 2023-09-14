twilio-wake-sms
===============

## What this is about
The main purpose of this repo is to help future me set up an app using twilio more quickly than last time
(if I have to do this again). The repo is not as friendly as it could be.
If someone else finds this repo helpful, then that's just bonus.

This repo contains code to set up twilio to make a call using crontab-ui.  It also contains code
to send twilio SMS messages using contrab-ui.  The code uses the elevenlabs API
for text to speech.

It is partially documented and not complete.

Below you will find some commands that may be helpful in getting this code to work

```bash
sudo apt update
```

```bash
sudo apt install ffmpeg
```

## set machine's timezone and restart

```bash
sudo dpkg-reconfigure tzdata
sudo service cron restart
```

Verify your date settings
```bash
timedatectl 
```

Reboot so that time works correctly
```bash
sudo shutdown -r now
```

```bash
pip install twilio
```

```bash
pip install elevenlabs
```

```bash
pip install google-cloud-storage
```