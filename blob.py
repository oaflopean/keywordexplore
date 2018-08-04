from textblob import TextBlob
import json



i = 0


a = open("booklist", mode="r")
b = open("Gutenberg.json", mode="r")
c = open("keywords", mode="w")
d = open("titles", mode="w")
booklist = json.load(a)
sentiments = {}
for book in booklist:
    blob = TextBlob(booklist[book])
    sentiment=blob.sentiment
    sentiments[book] = {}
    for name in sentiment._fields:
        sentiments[book][name]=getattr(sentiment, name)
e = open("sentiment-titles", mode="w")
json.dump(sentiments, e)