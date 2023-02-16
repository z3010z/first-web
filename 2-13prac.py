import requests
from bs4 import BeautifulSoup
import sys
import pymongo

article = []
last_page_link = ""
time = 0

if int(sys.argv[1]) > 5000 :
    time = 5000
else :
    time = int(sys.argv[1])

def capData() :
    r = requests.get("https://www.ptt.cc/bbs/joke/index.html")
    
    global time
    #在def裡，需要告訴這是def外的全域變數
    while time > 0:
        
        soup = BeautifulSoup(r.text,"html.parser")
        index_soup = soup.select("div.title a")
        #首頁的第一個標題 EX:[購機] 智慧手環推薦

        last_page_soup = soup.select("a.btn")
        #上一頁

        for l in last_page_soup:
            if "‹ 上頁" == l.text  :
                last_page_link = l["href"]

        for i in index_soup:
            r = requests.get("https://www.ptt.cc"+i["href"])
            
            soup = BeautifulSoup(r.text,"html.parser")
            #print(soup)
            article_soup = soup.select("div#main-content")

            article.append({ "html" : str(article_soup), "link" : i["href"] })
            #print(article_soup)


        r = requests.get("https://www.ptt.cc"+last_page_link)
        time -= 1
        print(time)
        #print(len(article_link))

def saveToDB() :
    # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    myclient = pymongo.MongoClient("mongodb+srv://jasonyaya:jasonyaya@cluster0.rjbp5vy.mongodb.net")

    mydb = myclient["fk"]

    mycol = mydb["fk0205"]
    
    mycol.insert_many(article)

def main() :
    capData()
    saveToDB()
    print("Total article : " + str(len(article)))

print( __name__ == '__main__')
    
# if __name__ == '__main__':
#     main()