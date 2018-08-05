from rake_nltk import Rake
from summarize import summarize
import json
from itertools import islice
import os

a = open("booklist", mode='r')
booklist = json.load(a)

for book in sorted(booklist.keys()):
    n = 300
    page_num = 0
    location = "/home/oaflopean/Gutenberg/paginated/"
    if os.path.exists(location+book+"/") == False:
        os.mkdir(location + book + "/")

        with open("/home/oaflopean/Gutenberg/clean/" + book + ".txt") as f:
            """
            try:
                next_n_lines = list(islice(f, n))
            except UnicodeDecodeError:
                foo=f.read()
                g = open(location+book+'txt', 'w')
                g.write(foo.encode('utf8'))
                f.close()
                f=g
                next_n_lines = list(islice(f, n))
    """
            while True:
                try:
                    next_n_lines = list(islice(f, n))
                except UnicodeDecodeError:

                        log=open("log.txt", mode="a")
                        log.write(book+"\n")
                        break
                page_text =" ".join(next_n_lines)
                if not next_n_lines:
                    break
                page_num += 1
                print(book + " page " + str(page_num))
                pg = {}
                pg["page_num"] = page_num
                pg["text"] = page_text
                pg["keywords"] = []
                r = Rake()
                r.extract_keywords_from_text(pg["text"])
                print("processing keywords")
                phrases = r.get_ranked_phrases()
                for phrase in phrases[:10]:
                    pg["keywords"].extend(phrase.split(" "))
                unique=set(pg["keywords"])
                pg["keywords"]=list(unique)
                summary = summarize(page_text, sentence_count=1, language='english')
                pg["summary"] = summary

                file = open(location + book + "/page_" + str(page_num) + ".json", mode="w")
                json.dump(pg, file, indent=4, ensure_ascii=True)
    else:
        continue