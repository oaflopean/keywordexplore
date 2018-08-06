import os
from os import listdir
from os.path import isfile, join
import json
json_file = open("booklist", "r")
gutenbergjsonstring=json_file.read()
d=json.loads(gutenbergjsonstring)
from google.cloud import storage
from google_images_download import google_images_download
import json


f=open("kw_data.json","r")
kw_data=json.load(f)

storage_client = storage.Client()
bucket = storage_client.get_bucket("babelli-keywords")
# Accumulate the iterated results in a list prior to issuing
# batch within the context manager
current_blobs = [blob for blob in bucket.list_blobs()]
already_upl=[]
all_kw=[]
path = "keywords-icons-large/"

for blobs in current_blobs:
    already_upl.append(blobs.name)
print(already_upl)
kw_data_list = list(kw_data.keys())
print("length of all_kw= " + str(len(all_kw)))
for kw1 in kw_data_list:
    kw_file = "keywords/" + kw1 + ".jpg"
    if kw_file not in already_upl:
        all_kw.append(kw1)
with storage_client.batch():
    print("length of all_kw= " + str(len(all_kw)))
    for kw2 in all_kw:
        new_blob = bucket.blob("keywords/"+kw2 + ".jpg")
        try:
            onlyfiles = [f for f in listdir(path + kw2 + "/") if isfile(join(path + kw2, f))]
        except FileNotFoundError:
            continue
        print("Uploading "+kw2)
        try:
            new_blob.upload_from_filename(path+kw2+"/"+onlyfiles[0])
        except IndexError:
            continue


"""


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
    print("Gathering keywords: "+str(book))
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
kw_icons=[]
kw_json={}
seen = set(kw_json.keys())
for key in keywords2.keys():
    kw_icons=keywords2[key]
    for item in kw_icons:
        if item not in seen:
            seen.add(item)
            kw_json[item]=[key]
        else:
            kw_json[item].append(key)
    print("Organized keywords: "+key)

e=open("keywords.json", mode="w")
json.dump(kw_json,e, indent=4)

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
                

f=open("keywords.json","r")
kw_json=json.load(f)

kw_data={}
for key in kw_json.keys():
    num=len(kw_json[key])
    kw_data[key]={"results":kw_json[key],"num":num}

f.close()
f=open("kw_data.json","w")
json.dump(kw_data,f, indent=4)
"""