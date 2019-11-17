#coding = utf-8
#  ¥   RMB符号
import requests
import re
import bs4
from bs4 import BeautifulSoup

def getHTMLtext(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt, html):
    
    return 0


def printGoodsList(ilt):
    print("")

def saveGoodsList():

    return 0













if __name__ == "__main__":
    goods = "书包"
    depth = 3
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44*i)
            html = getHTMLtext(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
    saveGoodsList(infoList)