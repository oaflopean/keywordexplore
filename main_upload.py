import os
from os import listdir
from os.path import isfile, join
import json
json_file = open("booklist", "r")
gutenbergjsonstring=json_file.read()
d=json.loads(gutenbergjsonstring)
import requests
from google.cloud import storage
from google_images_download import google_images_download
import json

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))


response = google_images_download.googleimagesdownload()
i = 0


a = open("booklist", mode="r")
b = open("Gutenberg.json", mode="r")
c = open("keywords", mode="w")
d = open("titles", mode="w")
booklist = json.load(a)
Gutenberg = json.load(b)
stopwords=[ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]
keywords2={}

for book in booklist:
    keywords2[book]=[]
    try:
        titles=Gutenberg[book]["title"].lower()
        authors=Gutenberg[book]["author"]
        subjects=" ".join(Gutenberg[book]["subjects"]).lower()
        listofwords=[]
        try:
            listofwords=titles.split()+authors.split()+subjects.split()
            listofwords=set(listofwords)
            listofwords=list(listofwords)
            for y in listofwords:
                if y in stopwords:
                    listofwords.remove(y)


        except TypeError:
            continue

    except AttributeError:
            continue
    keywords3=" ".join(listofwords).replace(".","").replace(")","").replace("(","").replace("--","").replace(",","").replace("\"","").replace(":","").replace("—","")
    for kw in keywords3.split(" "):
        keywords2[book].append(kw)

a.close()
b.close()
c.close()
d.close()
for id in sorted(booklist):

    for kw in keywords2[id]:
        print(kw)
        url="http://storage.googleapis.com/babelli-keywords/keywords/"
        path="keywords-icons-large/"
        try:
            onlyfiles = [f for f in listdir(path + kw+"/") if isfile(join(path + kw, f))]
            print(onlyfiles)
        except FileNotFoundError:
            continue
        request = requests.get(url+kw+".jpg")
        if request.status_code == 200:
            print(str(id)+' already uploaded')
            continue
        else:
            try:
                upload_blob("babelli-keywords", path+kw+"/"+onlyfiles[0], "keywords/"+kw+".jpg")
            except IndexError:
                print("error on keyword: "+kw)
                continue
