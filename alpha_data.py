import requests,html5lib
from bs4 import BeautifulSoup as bs
import re

url="https://en.wikipedia.org"
alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N-O','O','P','Q-R','R','S','T','U','V','W','X','Y','Z']
for i in range(len(alp)):
    alpha=alp[i]
    search="https://en.wikipedia.org/wiki/List_of_films:_"+alpha
    print(search)
    delimiter = "-",",",".","_",";",":"
    pattern='|'.join(map(re.escape,delimiter))
    r=requests.get(search)
    soup=bs(r.content,'html5lib')
    for link in soup.find_all("div",{"class":"div-col columns column-width"}):
        a=[]
        for x in link.find_all("li"):
            v=x.text
            v=''.join(re.split(pattern,v))
            #print(v)
            #a.append(v)
            with open("E:/VIT 2016/6th sem/sub/data/ {}.txt".format(alpha),"a",encoding="utf-8") as f:
                if(v[0]==alpha[0]):
                    f.write(v)
                    f.write("\n")
    
