#!/usr/bin/env python3

import sys
from urllib.parse import urlparse

from google.cloud import storage

def delete_gcs_object(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()
    print(f"Blob {blob_name} deleted from {bucket_name}.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python script_name.py [GCS_URL]')
        sys.exit(1)

    gcs_url = sys.argv[1]
    parsed_url = urlparse(gcs_url)


        # Extract bucket name and blob name from the URL
    bucket_name = parsed_url.path.split('/')[1]
    blob_name = '/'.join(parsed_url.path.split('/')[2:])

    # Authenticate using the service account credentials
    # Ensure GOOGLE_APPLICATION_CREDENTIALS environment variable is set or you are authenticated
    delete_gcs_object(bucket_name, blob_name)
