from bs4 import BeautifulSoup
from .Except import PeribahasaTidakDitemukan
import requests
class peribahasa:
    def __init__(self, peribahasa_, arti) -> None:
        self.peribahasa = peribahasa_
        self.arti = arti
        self.js = {
            "peribahasa":self.peribahasa,
            "arti":self.arti
        }
    def __getitem__(self, key):
        return self.js[key]
    def __setitem__(self, key, value):
        self.js[key] = value
    def __delitem__(self, key):
        del self.js[key]
    def update(self, dicti):
        self.js.update(dicti)
    def __iter__(self):
        return iter(self.js)
    def __len__(self):
        return len(self.js)
    def __str__(self) -> str:
        return f"<[peribahsa: {self.peribahasa[:7]}{'...' if len(self.peribahasa)>7 else ''}  arti: {self.arti[:7]}{'...' if len(self.arti)>7 else ''} ]>"
    def __repr__(self) -> str:
        return self.__str__()
def cari(query:str):
    try:
        p=[]
        req=requests.post("https://jagokata.com/peribahasa/cari.html", data={"carikata":query,"zoekbutton":"Zoeken"})
        parse = BeautifulSoup(req.text, "html.parser")
        for i in parse.find_all("ul",attrs={"class":"peribahasa"})[0].find_all("li"):
            if i.i:
                p+=[peribahasa(i.text, i.i.text[1:])]
        return p
    except IndexError:
        raise PeribahasaTidakDitemukan("!!")