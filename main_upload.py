from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from selenium.common.exceptions import NoSuchElementException
import urllib.request, urllib.parse, urllib.error
import urllib.request
import http.client
json_file = open("booklist", "r")
gutenbergjsonstring=json_file.read()
d=json.loads(gutenbergjsonstring)
import requests
from google.cloud import storage
import os
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

for id in sorted(d.keys()):
    url="http://storage.googleapis.com/babelli-covers/"

    if os.path.isfile(str(id)+"_small.jpg") and os.path.isfile(str(id)+"_medium.jpg"):
        request = requests.get(url+str(id)+"_small.jpg")
        if request.status_code == 200:
            print(str(id)+' already uploaded')
            continue
        else:
            upload_blob("babelli-covers", "covers/"+str(id)+"_small.jpg", str(id)+"_small.jpg")
            upload_blob("babelli-covers", "covers/"+str(id)+"_medium.jpg", str(id)+"_medium.jpg")
    else:
        print(str(id)+" not found")
