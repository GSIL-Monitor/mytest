# -*- coding:utf-8 -*-
author = 'chenshu2'
import pymysql
import requests

def tryconnect():
    #unix_socket='/tmp/mysql.sock'
    con = pymysql.connect(host = "localhost",user= 'root',password=None,db='mytest')
    cur = con.cursor()
    cur.execute("USE mytest")
    cur.execute("select * from pages where id = 1")
    print(cur.fetchall())
    cur.close()
    con.close()
    pass

#存储维基百科数据
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
def trystoragewiki():
    con = pymysql.connect(host = "localhost",user= 'root',password=None,db='mytest',charset = 'utf8')
    cur = con.cursor()
    cur.execute("use mytest")
    random.seed(datetime.datetime.now())
    def store(title,content):
        sql = "insert into pages(title,content) values('"+ title +"','"+ content +"')"
        cur.execute(sql)
        cur.connection.commit()
    def getLinks(articleurl):
        html = urlopen("http://en.wikipedia.org" + articleurl)
        bsobj = BeautifulSoup(html)
        title = bsobj.find("h1").get_text()
        content = bsobj.find("div",{"id":"mw-content-text"}).find("p").get_text()
        store(title,content)
        return bsobj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
    links = getLinks("/wiki/Kevin_Bacon")
    try:
        while len(links) > 0:
            newArticle = links[random.randint(0,len(links) -1)].attrs["href"]
            print(newArticle)
            links = getLinks(newArticle)
    finally:
        cur.close()
        con.close()

#不超过6的维基百科页面存储起来
def trybenken():
    conn = pymysql.connect(host = "localhost",user= 'root',password=None,db='mytest',charset = 'utf8')
    cur = conn.cursor()
    cur.execute("use wikipedia")
    def insertpageInfoExists(url):
        cur.execute("select * from pages where url = %s",(url))
        if cur.rownumber == 0:
            cur.execute("insert into pages (url) values (%s)",(url))
            conn.commit()#提交事务
            return cur.lastrowid
        else:
            return cur.fetchone()[0]

    def insertLink(fromPageId,toPageId):
        cur.execute("select * from links where frompageid = %s and toPageId = %s",(int(fromPageId),int(toPageId)))
        if cur.rowcount == 0:
            cur.execute("insert into links (frompageId,toPageId) values (%s,%s)",(int(fromPageId),int(toPageId)))
            conn.commit()

    pages = set()
    def getLinks(pageurl,recursionlevel):
        if recursionlevel > 4:
            return
        pageId = insertpageInfoExists(pageurl)
        html = requests.get("http://en.wikipedia.org" + pageurl)
        bsobj = BeautifulSoup(html.text)
        for link in bsobj.findAll("a",href = re.compile("^(/wiki/)((?!:).)*$")):
            insertLink(pageId,insertpageInfoExists(link.attrs['href']))
            if link.attrs['href'] not in pages:
                #遇到一个新的页面加入集合并搜索里面的词条链接
                newpage = link.attrs['href']
                pages.add(newpage)
                getLinks(newpage,recursionlevel + 1)
    getLinks("/wiki/Kevin_bacon",0)
    cur.close()
    conn.close()

if __name__ == '__main__':
    trybenken()

