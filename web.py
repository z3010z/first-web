import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
#print(r.text)

soup = BeautifulSoup(r.text,"html.parser")

#print(soup)
sel = soup.select("div.title a")
#dic 中抓 title 裡面span的tag (沒span就是把title裡面全部抓下來)
print(sel)

for s in sel:
    print(s["href"],"  -  ", s.text)
    print("~~~~")