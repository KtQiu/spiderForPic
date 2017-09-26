#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2017/9/26 19:57
# @Author   : Kt Qiu
# @File     : testSpider.py
# @Email    : kitty666ball@gmail.com



# 2017-9-26 21:55:30
# Something is just wrong.
import re
import requests

maxSearchPage = 10
CurrentPage = 0
defaultPath = "D:/Files/spider/test"
NeedSave = 1


def imageFiler(content):
    return re.findall('"objURL":"(.*?)"', content, re.S)


def nextSource(content):
    next = re.findall('<div id="page">.*<a href="(.*?)" class="n">', content, re.S)[0]
    print("________" + "http://image.baidu.com" + next)
    return next


def spider(source):
    content = requests.get(source).text
    imageArr = imageFiler(content)
    global CurrentPage
    print("Current page:" + str(CurrentPage) + "*******************")
    for imageUrl in imageArr:
        print(imageUrl)
        global NeedSave
        if NeedSave:
            global DefaulPath
            try:
                picture = requests.get(imageUrl, timeout=10)
            except:
                print("Download image error! errorUrl:" + imageUrl)
                continue
            pictureSavePath = defaultPath + imageUrl.replace('/', '')
            fp = open(pictureSavePath, 'wb')
            fp.close()
        else:
            global maxSearchPage
            if CurrentPage <= maxSearchPage:
                if nextSource(content):
                    CurrentPage += 1
                    spider("http://image.baidu.com" + nextSource(content))


def beginSearch(page=1, save=0, savePath="D:/Files/spider/test"):
    global maxSearchPage, NeedSave, defaultPath
    maxSearchPage = page
    NeedSave = save
    defaultPath = savePath
    key = input("Plz input the keywords to search: ")
    StartSource = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=" + str(key) + "&ct=201326592&v=flip"
    spider(StartSource)


beginSearch(page=2, save=0)
