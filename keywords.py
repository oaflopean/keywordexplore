import json

a = open("booklist", mode="r")
b = open("Gutenberg.json", mode="r")
c = open("keywords", mode="w")
d = open("titles", mode="w")
booklist = json.load(a)
Gutenberg = json.load(b)
stopwords=[ "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "could", "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "it", "it's", "its", "itself", "let's", "me", "more", "most", "my", "myself", "nor", "of", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "she'd", "she'll", "she's", "should", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "we'd", "we'll", "we're", "we've", "were", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "would", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves" ]

for book in booklist:
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
    c.write(book + " " + " ".join(listofwords).replace(".","").replace(")","").replace("(","").replace("--","").replace(",","").replace("\"","").replace(":","").replace("—","")+"\n")

for book in booklist:
    d.write(str(book)+" "+booklist[book]+"\n")


a.close()
b.close()
c.close()
d.close()