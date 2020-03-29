import nltk
import re

words = {}
# r = re.compile(r"[,!\*\.]")

with open("test.txt","r",encoding='utf-8') as f:
    # for line in f:
    #     for word in r.sub("",line.strip()).split(" "):
    #         if word in words:
    #             words[word] += 1
    #         words.setdefault(word,1)
    for line in f:
        line = re.sub(r"[0-9]+", " ", line)
        word1 = re.sub(r"([^A-Za-z\s])+","", line.strip()).split()
        for word in word1:
            word=word.lower()
            if word in words:
                words[word] += 1
            words.setdefault(word, 1)

stopwords=open(r"stopwords.txt",'r')
s=set()
for stopword in stopwords:
    stopword=stopword.replace('\n','')
    s.add(stopword)

for key in list(words.keys()):
    if set(key).issubset(stopword):
        del words[key]
stopwords.close()


for word2,count in words.items():
    print(word2,count)


