#!/usr/bin/env python
# -*- coding: utf-8 -*-



from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random

client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji']
url_list_three = ganji['url_list_three']
item_info = ganji['item_info']


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
    'Referer' : 'http://bj.ganji.com/wu/'
}



def get_first_links(list_url,pages,who='o'):#导出所有的正常页面
    #'http://bj.ganji.com/jiaju/o3/'
    link_url = '{}{}{}/'.format(list_url,str(who),str(pages))
    time.sleep(1)
    wb_data = requests.get(link_url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'html5lib')
    #if soup.find('ul','pageLink'):
    for link in soup.select('dl.list-bigpic  > dt > a'):
        third_links = link.get('href')
        if 'Mzhuanzhuan' in third_links:
            pass
        else:
            url_list_three.insert_one({'url': third_links})
            print(third_links)
#else:
    #pass



#获取页面数据

def get_all_data(url,data=None):
    wb_data = requests.get(url,headers=headers)
    if wb_data.status_code == 404:
        pass
    else:
        try:

            soup = BeautifulSoup(wb_data.text,'html5lib')
            data = {
                'title': soup.select('.title-name')[0].text,
                'pub_data':soup.select('.title-info-l')[0].text.strip().split(' ')[0],
                'cates':soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].text.strip(),
                'area':list(map(lambda x:x.text,soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
                'price':soup.select('ul.det-infor > li:nth-of-type(2) > i.f22.fc-orange.f-type')[0].text,
                'url':url
            }
            item_info.insert_one(data)
            print(data)
        except (TypeError, SyntaxError):
            pass

