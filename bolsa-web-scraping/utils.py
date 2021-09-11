import requests
from datetime import datetime
from google.cloud import storage

def concate_strings(*argv):
    return ''.join(arg for arg in argv)

def get_current_date(BTZ):
    datetime_utc = datetime.now(BTZ)
    current_date = datetime_utc.strftime("%d%m%Y")

    return current_date

def download_zip_file(url, final_file_name):
    r = requests.get(url, verify=False)

    return r.content

def save_to_gcs(bucket_name, final_file_name, content):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(final_file_name)
    blob.upload_from_string(content)