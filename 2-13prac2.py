import requests
from bs4 import BeautifulSoup
import sys
import pymongo

article = []
C = 0
# L = ""
r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
while C < 3:

    soup = BeautifulSoup(r.text,"html.parser")
    sel = soup.select("div.title a")
    L = soup.select("a.btn")
    for l in L:
        if "‹ 上頁" in l.text  :
            L = l["href"]

    for i in sel:
        R = requests.get("https://www.ptt.cc"+i["href"])
        Soup = BeautifulSoup(R.text,"html.parser")
        article_soup = Soup.select("div#main-content")
        article.append({ "html" : str(article_soup), "link" : i["href"] })
    r = requests.get("https://www.ptt.cc"+L)
    C = C+1
    print(C)
myclient = pymongo.MongoClient("mongodb+srv://jasonyaya:jasonyaya@cluster0.rjbp5vy.mongodb.net")

mydb = myclient["三上悠亞"]

mycol = mydb["阿阿阿"]
    
mycol.insert_many(article)

print("Total article : " + str(len(article)))

