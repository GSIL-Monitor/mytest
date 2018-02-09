# -*- coding:utf-8 -*-

author = 'chenshu2'
import requests
import re
import pymysql
from urllib.request import urlopen
from bs4 import BeautifulSoup

def search_m_train():
    html = urlopen("http://m.tuniu.com/train")
    bsobj = BeautifulSoup(html,"html.parser")
    #print(bsobj)
    for link in bsobj.findAll("div"):
        print(link)






if __name__ == '__main__':
    search_m_train()