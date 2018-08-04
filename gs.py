from google_images_download import google_images_download

import json

import urllib
import urllib.request
from string import punctuation
import string
import os
import time
import os.path
json_file = open("booklist", "r")
gutenbergjsonstring = json_file.read()
d = json.loads(gutenbergjsonstring)

response = google_images_download.googleimagesdownload()
i = 0

for id in sorted(d.keys()):
    ls = time.time()
    if os.path.isdir("covers-medium/" + str(id)) or os.path.isfile("/home/oaflopean/PycharmProjects/webscraper/covers/"+str(id)+"_medium.jpg"):
        print(str(id) + " exists")
        i = i + 1
        n = (i * 100) / len(d.keys())
        print(str(n) + "% done")
    else:
        string = d[id].replace(",", "")
        arguments = {"keywords": string + " classic book cover image", "aspect_ratio": "tall", "thumbnail": 1,
                     "limit": 1, "size": "medium", "output_directory": "covers-medium",
                     "image_directory": id}  # creating list of arguments
        paths = response.download(arguments)
        i = i + 1
        n = (i * 100) / len(d.keys())
        hs = time.time()
        timerunning = hs - ls
        hours =(int(timerunning) * (len(d.keys()) - i)) / 60 /60
        print(str(id)+"<--- ID NUMBER")
        print(str(round(n)) + "% done " + str(round(hours)) + " hours remaining")
