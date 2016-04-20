#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


first_url = 'http://bj.ganji.com/wu/'
host_url = 'http://bj.ganji.com'

def get_first_pages(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for second_url in soup.select('.fenlei > dt > a'):
        list_url = host_url + second_url.get('href')
        print(list_url)

get_first_pages(first_url)

list_url = '''
    http://bj.ganji.com/jiaju/
    http://bj.ganji.com/rirongbaihuo/
    http://bj.ganji.com/shouji/
    http://bj.ganji.com/shoujihaoma/
    http://bj.ganji.com/bangong/
    http://bj.ganji.com/nongyongpin/
    http://bj.ganji.com/jiadian/
    http://bj.ganji.com/ershoubijibendiannao/
    http://bj.ganji.com/ruanjiantushu/
    http://bj.ganji.com/yingyouyunfu/
    http://bj.ganji.com/diannao/
    http://bj.ganji.com/xianzhilipin/
    http://bj.ganji.com/fushixiaobaxuemao/
    http://bj.ganji.com/meironghuazhuang/
    http://bj.ganji.com/shuma/
    http://bj.ganji.com/laonianyongpin/
    http://bj.ganji.com/xuniwupin/
    http://bj.ganji.com/qitawupin/
    http://bj.ganji.com/ershoufree/
    http://bj.ganji.com/wupinjiaohuan/
'''
