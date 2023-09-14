#!/usr/bin/env python3

import sys
import os
import tempfile
from google.cloud import storage
from elevenlabs import generate, save, set_api_key
from secret import ELEVEN_API_KEY
from secret import BUCKET_NAME
import subprocess

BASE_URL = "https://storage.googleapis.com/"

def run_convert_audio(text_parameter):
    # Run the generate-audio.py script and capture its stdout                                                   
    result = subprocess.run(['./convert-wav-to-mp3.py', text_parameter], capture_output=True, text=True)

    # Check if the process executed successfully                                                                
    if result.returncode != 0:
        print("Error while converting to mp3 audio:", result.stderr)
        sys.exit(1)

    # Extract the URL value from stdout                                                                         
    mp3_filename = result.stdout.strip()
    return mp3_filename


# Ensure the user provided the necessary arguments
if len(sys.argv) < 2:
    print("Usage: generate-audio.py 'text_to_generate_audio'")
    sys.exit(1)

text_to_generate = sys.argv[1]

set_api_key(ELEVEN_API_KEY)

audio = generate(
    text=text_to_generate,
    voice="Bella",
    model="eleven_multilingual_v1"
)

# Creating a temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
output_filename = temp_file.name

# Saving the generated audio to the temp file
save(audio, output_filename)
mp3_filename = run_convert_audio(output_filename)

# Uploading to Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the specified Google Cloud Storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    # Make the blob publicly readable
    blob.make_public()
    

destination_file_name = os.path.basename(mp3_filename)
upload_blob(BUCKET_NAME, mp3_filename, destination_file_name)

# Output the name of the file that was uploaded to stdout
print(BASE_URL+BUCKET_NAME+"/"+destination_file_name)

# Deleting the temporary file after uploading to GCS
os.remove(output_filename)
os.remove(mp3_filename)
