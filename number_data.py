import requests,html5lib
from bs4 import BeautifulSoup as bs
import re

url="https://en.wikipedia.org"
alpha='numbers'
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
        if v not in a and v[0].isdigit():
            a.append(v)
    a=list(set(a))
    for i in a:
        with open("E:/VIT 2016/6th sem/sub/data/ {}.txt".format(alpha),"a",encoding="utf-8") as f:
            f.write(i)
            f.write("\n")
  
