import PIL
from google_images_download import google_images_download
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from selenium.common.exceptions import NoSuchElementException
import urllib
import urllib.request
from string import punctuation
import string
import os
from os import listdir
from os.path import isfile, join
from PIL import Image

json_file = open("booklist", "r")
gutenbergjsonstring = json_file.read()
d = json.loads(gutenbergjsonstring)

path = "covers-medium/"
for id in sorted(d.keys())[18521:]:
    if os.path.isdir(path + id):
        try:
            onlyfiles = [f for f in listdir(path + id) if isfile(join(path + id, f))]
            try:
                img1 = Image.open(path + id + "/" + str(onlyfiles[0])).convert('RGB').save(
                    "covers/" + id + '_medium.jpg')
            except OSError:
                continue
            img = Image.open("covers/" + id + "_medium.jpg")
            basewidth = 300
            wpercent = (basewidth / float(img.size[1]))
            hsize = int((float(img.size[0]) * float(wpercent)))
            img = img.resize((hsize, basewidth), PIL.Image.ANTIALIAS)
            img.save("covers/" + id + '_medium.jpg')
            print("medium: " + id)
        except IndexError or FileNotFoundError:
            continue
    else:
        continue
    try:
        onlyfiles = [f for f in listdir(path + id + " - thumbnail") if isfile(join(path + id, f))]
        img2 = Image.open(path + id + " - thumbnail/" + str(onlyfiles[0])).convert('RGB').save(
            "covers/" + id + '_small.jpg')
        img3 = Image.open("covers/" + id + "_small.jpg")
        basewidth = 100
        wpercent = (basewidth / float(img3.size[1]))
        hsize = int((float(img3.size[0]) * float(wpercent)))
        img4 = img3.resize((hsize, basewidth), PIL.Image.ANTIALIAS)
        img4.save("covers/" + id + '_small.jpg')
        print("small: " + id)
    except OSError:
        break
