import json
import os
titles=json.load(open("booklist"))
"""
path="texts"
for book in list(titles.keys()):
    os.system("wget http://storage.googleapis.com/babelli-epubs/text/"+str(book)+".txt ")
    f=open(str(book)+".txt", mode='r')
    p=open(path+"/"+titles[book][:10], mode='w')
    gut=False
    try:
        for line in f:
            if gut is True and  "***" in line.split(" "):
                break
            else
                if "***" not in line.split(" "):
                    p.write(line)
                else:
                    gut=True
    except UnicodeDecodeError:
        continue
    f.close()
    p.close()
    os.system("rm "+str(book)+".txt")
"""
a=open("booklist-r.txt",mode="w")
for book in titles:
    a.write(book+", ")
