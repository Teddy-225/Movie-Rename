import requests
import html5lib
from bs4 import BeautifulSoup as bs

name=input()
search="https://www.yifysubtitles.com/search?q="+name.replace(" ","+")
url="https://www.yifysubtitles.com"
print(search)

r=requests.get(search)
soup=bs(r.content,'html5lib')
#print(soup.prettify())

for link in soup.find_all("div",{"class":"media-body"}):
    choice=link.find('a')['href']
    movie_link=url+choice
    #print("url: {}".format(movie_link))
    go_next=requests.get(movie_link)
    soup_again=bs(go_next.content,'html5lib')
    #print(soup_again.prettify())
    for links in soup_again.find_all("tr",{"class":"high-rating"}):
        for x in links.find("td",{"class":"flag-cell"}):
            if(x.text=="English"):
                for download in links.find_all("td",{"class":"download-cell"}):
                    path=download.find('a')['href']
                    download_link=url+path
                    print("subtitle link: ",download_link)

                download_page=requests.get(download_link)
                soup3=bs(download_page.content,'html5lib')
                #print(soup3.prettify())
                for tag in soup3.find_all("div",{"class":"col-xs-12"}):
                    for btn in tag.find_all("a",{"class":"btn-icon download-subtitle"}):
                        print("link :",btn.get('href'))
                        final=btn.get('href')
                        get_sub=requests.get(final)
                        with open("E:/VIT 2016/6th sem/sub/ {}.zip".format(name),'wb') as f:
                            content=f.write(get_sub.content)
                            print("Downloaded file: ",content)
    
