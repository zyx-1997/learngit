import os
import os.path
import re

list=[]
word1={}

def read_file(path,list):
    file_list=os.listdir(path)
    for file_name in file_list:
        path2=os.path.join(path,file_name)
        if os.path.isdir(path2):
            read_file(path2,list)
        else:
            with open(path2,'r',encoding='utf-8',errors='ignore') as f:
                file_data=f.read()
                list.append(file_data)

def count(txt):
     r = re.compile(r"[,!\*\.]")
     for line in txt:
        words=r.sub("",line.strip()).split(" ")
        for word in words:
            if word in word1:
                word1[word]+=1
            word1.setdefault(word,1)



path='D:\\lab1-feature-selection\\20news-bydate'
read_file(path,list)
list='\n'.join(list)
length=len(list.splitlines())
print(list)
print(length)

with open("test.txt", "w",encoding='utf-8') as f:
    f.write(list)
with open("test.txt", "r",encoding='utf-8') as f:
    count(f)
print(word1)