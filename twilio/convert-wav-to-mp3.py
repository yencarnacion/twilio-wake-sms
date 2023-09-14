#!/usr/bin/env python3

import sys
import subprocess

def convert_wav_to_mp3(wav_file):
    # Ensure file has .wav extension
    if not wav_file.endswith('.wav'):
        print("Error: Provided file does not have .wav extension")
        return
    
    # Extract the name without the extension
    output_file = wav_file.replace('.wav', '.mp3')

    # Execute the ffmpeg command
    cmd = ['/usr/bin/ffmpeg', '-i', wav_file, '-acodec', 'libmp3lame', output_file]
    try:
        subprocess.run(cmd, check=True)
        print(output_file)  # Print the name of the output mp3 file
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

if __name__ == "__main__":
    # Check if filename is provided
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <filename>.wav")
        sys.exit(1)

    wav_file = sys.argv[1]
    convert_wav_to_mp3(wav_file)
