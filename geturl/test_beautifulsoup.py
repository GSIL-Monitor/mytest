# -*- coding:utf-8 -*-
author = 'chenshu2'
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import re
import datetime
import random
from urllib.request import urlretrieve
import os

def test(url):
    #html = requests.get(url="http://en.wikipedia.org/wiki/Kenvin_Bacon")
    html = requests.get("http://en.wikipedia.org/" + url)
    bsobj = BeautifulSoup(html.text)
    #print(bsobj.findAll('a')[0].attrs)
    '''
    for link in bsobj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])
    '''
    return bsobj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
def test_2():
    html = urlopen(url="https://m.tuniu.com/train")
    bsobj = BeautifulSoup(html)
    for a in bsobj.findAll("div"):
        if 'id' in a.attrs:
            print(a.attrs['id'])
    pass

def gettest():
    random.seed(datetime.datetime.now())
    links = test("/wiki/Kevin_Bacon")
    while len(links) > 0:
        newurl = links[random.randint(0, len(links) - 1)].attrs["href"]
        print(newurl)
        links = test(newurl)
    pass

'''
避免一个页面被采集两次，链接去重
把已发现的链接都放在一起，并保存结果，
set类型
'''
pages = set()
def getset(pageurl):
    global pages
    html = requests.get("http://en.wikipedia.org" + pageurl)
    bsoobj = BeautifulSoup(html.text)
    for link in bsoobj.findAll("a",href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            #print(link.attrs['href'])
            if link.attrs['href'] not in pages:
                print(link.attrs['href'])
                newpage = link.attrs['href']
                pages.add(newpage)
                getset(newpage)

    pass
    '''
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                gettest(newPage)
    '''

#区分不同页面

def getlinkslists(pageurl):
    global pages
    html = requests.get("http://en.wikipedia.org" + pageurl)
    bsobj = BeautifulSoup(html.text)
    try:
        print(bsobj.h1.get_text())
        print(bsobj.find(id = "mw-content-text").findAll("p")[0])
        print(bsobj.find(id = "ca-edit").findAll("span").find("a").attrs['href'])
    except AttributeError:
        print("\n页面缺少一些属性！不过不用担心！")
    for link in bsobj.findAll('a',href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #我们遇到了新的页面
                newpage = link.attrs['href']
                print("----------------------------\n" + newpage)
                pages.add(newpage)
                getlinkslists(newpage)

#网络爬虫,获取页面所有的内链
random.seed(datetime.datetime.now())
def getinternallinks(bsobj,includeurl):
    includeurl = urlparse(includeurl).scheme + "://" + urlparse(includeurl).netloc
    internallinks = []
    #找出所有/开头的链接
    for link in bsobj.findAll("a",href = re.compile("^(/|.*" + includeurl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internallinks:
                if (link.attrs['href'].startswith("/")):
                    internallinks.append(includeurl + link.attrs['href'])
                else:
                    internallinks.append(link.attrs['href'])
    return internallinks

#获取页面所有的外链的列表
def getexternallinks(bsobj,excludeurl):
    externallinks = []
    #找出所有以http或者www开头且不包含当前的url链接
    for link in bsobj.findAll("a",href = re.compile("^(http|www)((?!" + excludeurl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externallinks:
                externallinks.append(link.attrs['href'])
    return externallinks

def getRandomExternallinks(startingPage):
    html = requests.get(startingPage)
    bsobj = BeautifulSoup(html.text)
    externallinks = getexternallinks(bsobj,urlparse(startingPage).netloc)
    if len(externallinks) == 0:
        print("no external links,looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internallinks = getinternallinks(bsobj,domain)
        return getRandomExternallinks(internallinks[random.random(0,len(internallinks) - 1)])
    else:
        return externallinks[random.randint(0,len(externallinks) - 1)]

def followExternaOnly(startingSite):
    externallink = getRandomExternallinks(startingSite)
    print("Random external link is :" + externallink)
    followExternaOnly(externallink)

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

#收集页面上所有发现的外链
allExtlinks = set()
allIntlinks = set()
def getAllExternallinks(url):
    html = urlopen(url)
    bsobj = BeautifulSoup(html)
    internallinks = getinternallinks(bsobj,splitAddress(url)[0])
    externallinks = getexternallinks(bsobj,splitAddress(url)[0])
    for link in externallinks:
        if link not in allExtlinks:
            allExtlinks.add(link)
            print(link)
    for link in internallinks:
        if link not in allIntlinks:
            print("即将获取链接的url是：" + link)
            allIntlinks.add(link)
            getAllExternallinks(link)

#根据文件的url下载文件：
def downloadlogo():
    html = urlopen("http://www.pythonscraping.com")
    bsobj = BeautifulSoup(html)
    imagelocation = bsobj.find("a",id = "logo").find("img")["src"]
    urlretrieve(imagelocation,"logo.jpg")
    pass

#下载文件，获取文件类型
downloaddicrectory = "downloaded"
baseurl = "http://pythonscraping.com"
def getAbsoluteUrl(baseurl,source):
    if source.startswith("http://www."):
        url = "http://"  + source[11:] #第十一位开始
    elif source.startswith("http://"):
        url = source
    elif source.startswith('www.'):
        url = "http://" + source[4:]
    else:
        url = baseurl + "/"  + source
    if baseurl not in url:
        return None
    return url

#windows下文件名含有特殊字符如？的文件无法生成
def getDownloadPath(baseurl,absoluteurl,downloadDirectory):
    path = absoluteurl.replace("www.","")
    path = path.replace(baseurl,"")
    path = downloadDirectory + path
    index = path.find("?")
    path = path[:index]
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

def run_upper():
    html = urlopen("http://www.pythonscraping.com")
    bsobj = BeautifulSoup(html)
    downloadlist = bsobj.findAll(src = True)
    for download  in downloadlist:
        fileurl = getAbsoluteUrl(baseurl,download["src"])
        if fileurl is not None:
            print(fileurl)
            #文件名绝对路径，保存的路径+文件名
            urlretrieve(fileurl,getDownloadPath(baseurl,fileurl,downloaddicrectory))
    pass

#将获取的html文件表格保存为csv格式
import csv
def csv_case():
    html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
    bsobj = BeautifulSoup(html)
    #主对比表格是当前页面的第一个表格
    table = bsobj.findAll("table",{"class":"wikitable"})[0]
    rows = table.findAll("tr")
    csvFile = open("..//file/editors.csv","wt",newline="",encoding='utf-8')
    writer = csv.writer(csvFile)
    try:
        for row in rows:
            csvRow = []
            for cell in row.findAll(['td','th']):
                csvRow.append(cell.get_text)
            writer.writerow(csvRow)
    finally:
        csvFile.close()
    pass


if __name__ == '__main__':

    run_upper()


    pass
