import re
from concurrent.futures import ThreadPoolExecutor
from .Except import KataBijakTidakDitemukan
from bs4 import BeautifulSoup as bs
import requests
get_page = lambda g:list(set(re.findall("(https?://.*?\.html\?page=[0-9])\"", g)))
class author:
    def __init__(self, url, name, bio, img) -> None:
        self.name = name
        self.url = url
        self.bio = bio
        self.image = img
    def get_quotes(self):
        p = []
        resp = get_page(requests.get(self.url).text)
        for i in resp:
            p+=self.quote(i)
        return p
    def quote(self, url):
        p = []
        parse=bs(requests.get(url).text, "html.parser")
        for i in parse.find_all("q",attrs={"class":"fbquote"}):
            p.append(quote(self.name,self.url, self.bio,i.text, self.image))
        return p
    def __str__(self) -> str:
        return f"<(AUTHOR: {self.name})>"
    def __repr__(self) -> str:
        return self.__str__()

class quote:
    def __init__(self, profile_name, profile_url, bio, quote, img) -> None:
        self.quote = quote
        self.text = quote
        self.author = author(profile_url,profile_name, bio, img)
    def __str__(self) -> str:
        return f"<-[AUTHOR: {self.author.name} CAPT: {self.text[:9]}{'...' if len(self.text)> 9 else ''}]->"
    def __repr__(self) -> str:
        return self.__str__()
def parser(html):
    try:
        p=[]
        parse=bs(html, "html.parser")
        for i in parse.find_all("ul", attrs={"id":"citatenrijen"})[0].find_all("li"):
            if i.a and i.find_all("span",attrs={"class":"auteur-beschrijving"}) and i.img:
                key = "data-src" if i.img.get("data-src") else "src"
                p.append(quote( i.a.text, i.a["href"], i.find_all("span",attrs={"class":"auteur-beschrijving"})[0].text, i.q.text, i.img[key]))
        return p
    except IndexError:
        raise KataBijakTidakDitemukan("!!")
def carikata(kata:str, all_page=False, worker=5):
    p=[]
    req=requests.post("https://jagokata.com/kata-bijak/cari.html", data={"carikata":kata,"zoekbutton":"Zoeken"})
    p+=parser(req.text)
    if all_page:
        with ThreadPoolExecutor(worker) as wx:
            for i in get_page(req.text):
                p+=wx.submit(parser, requests.get(i).text).result()
    return p
