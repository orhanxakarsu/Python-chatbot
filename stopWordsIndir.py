from bs4 import BeautifulSoup,NavigableString, Tag
from fake_useragent import UserAgent
import requests

import csv


ua = UserAgent()
url ="https://www.turkceogretimi.com/genel-konular/turkce-etkisiz-kelimeler-stop-words-listesi-11"
glassdor =requests.get(url,ua.chrome)
jobs=glassdor.content
soup = BeautifulSoup(jobs,"html.parser")
kelimeler = soup.find_all("p",{"class":"MsoNormal"})

stopwordsKarisik=[]
for kelime in kelimeler :
    if isinstance(kelime, NavigableString):
        continue
    else:
        stopwordsKarisik.append(kelime.text)

sonDizi =[]
yeniDizi = stopwordsKarisik[0].split("\n")
for i in yeniDizi:
    sonDizi.append(i[:-1])

stopWords=[]

for word in sonDizi:
    if len(word)<=12 and len(word)!=0 :
        stopWords.append(word)
        

import json

data = {"stopWords":stopWords}


with open('veriler.json', 'w',encoding='utf-8') as f:
    json.dump(data, f)
