import os
import requests,html5lib
from bs4 import BeautifulSoup as bs
import re

path = 'E:/MOVIES'
#url="https://www.imdb.com"
delimiter = "-",",",".","_",";",":"," "
pattern='|'.join(map(re.escape,delimiter))

a=os.listdir(path)
movie_folder=a[:]
b=[]
for i in range(len(a)):
    a[i]=' '.join(re.split(pattern,a[i]))
    a[i]=a[i].capitalize()
    a[i]=a[i].replace("&","and")
    a[i]=a[i].lower()
b=a
#print(a)
#temp=b[4]
#temp=temp.split()
#print(a)
d=[]
#print(movie_folder)
with open("E:/VIT 2016/6th sem/sub/data/main.txt","r",encoding="utf-8") as f:
    for line in f:
        line=line.replace('\n','')
        line=line.replace("&","and")
        #line=line.replace(" ","")
        line=re.sub(r'\(.*\)', '', line)
        #re.sub("[\(\[].*?[\)\]]", "", line)
        line=line.rstrip()
        line=line.lower()
        d.append(line)
        #print(line)
#for i in x:
#print(len(d))
#print(d[3])
#print(len(b))
#print(b)
correct=[]
not_found=[]
#print(path)
for name in range(len(b)):
    flag=0
    temp=b[name]
    temp=temp.lower()
    temp=temp.split()
    #print(temp)
    for i in range(len(temp),-1,-1):
        if(flag!=1):
            part=' '.join(temp[0:i])
            #sam="Another Cinderella Story"
            #print(part)
            for data in range(len(d)):
                if(part==d[data] and d[data] not in correct and flag!=1):
                    flag+=1
                    #print(part)
                    correct.append(d[data])
                    if d[data]!='':
                        loc=os.path.abspath(path+'/'+movie_folder[name])
                        #print(loc)
                        os.rename(loc,path+'/'+d[data])
                        #print(d[data])
        if(flag==0):
            #print(movie_folder[name])
            if movie_folder[name] not in not_found:
                not_found.append(movie_folder[name])
#print(correct)
print(not_found)
#print(b)
#for x in range(len(d)):
    
#for movie_folder in a:
#search="https://www.imdb.com/search/title?title="+movie_folder.replace(" ","+")
#print(search)
#r=requests.get(search)
#soup=bs(r.content,'html5lib')
#print(soup.prettify)
