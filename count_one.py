#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
from page_parsing_one import url_list_three

while True:
    print(url_list_three.find().count())
    time.sleep(5)
