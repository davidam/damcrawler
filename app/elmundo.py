#!/usr/bin/python
# -*- coding: utf-8 -*-
from formatter import Formatter
from urlthread import UrlThread
from formatter import Formatter
from crawler import Crawler
from newspaper import Article
import os, logging, pdb, time
from pprint import pprint
from time import gmtime, strftime, time

if __name__ == "__main__":
    year = 2017
    month = 13
    day = 32

    m = []
    logging.basicConfig(filename='damcrawler.log', level=logging.INFO)    
#    pdb.set_trace()
    cwd = os.getcwd()
    curpath = cwd + "/../periodicos/elmundo"
    print(curpath)
    if (os.path.isdir(curpath)):
        os.chdir(curpath)
    else:
        os.makedirs(curpath)
        os.chdir(curpath)
    for i in range(1, month):
        if (i < 10):    
            m.append(["0"+str(i)])
            mstr = "0"+str(i)
        else:
            m.append([i])
            mstr = str(i)
        d = []
#        print(os.getcwd())
        for j in range(1, day):
            if (j < 10):
                d.append(["0"+str(j)])
                dstr = "0"+str(j)            
            else:
                d.append([j])
                dstr = str(j)
            url = "https://elmundo.es/elmundo/hemeroteca/2017/"+mstr+"/"+dstr+"/m/index.html"
            print(url)
            logging.info(url)
            path = mstr+"-"+dstr
            if (os.path.isdir(path)):
                print("Path is created")
                logging.info('Path is created')
            else:
                os.makedirs(path)
            os.chdir(path)
            
            c = Crawler(url)
            c.urlsLevelHost(2)
            for u in c.urls:
                caux = Crawler(u)
                faux = Formatter(u)
                name = faux.hostFromUrl() + str(time.time()) + ".xml"
                logging.info(faux.hostFromUrl() + str(time.time()))
                caux.downloadOneUrlNewspaperThread(name)
            os.chdir(curpath)

