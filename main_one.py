#!/usr/bin/env python
# -*- coding: utf-8 -*-


from multiprocessing import Pool
from channel_extracing_one import list_url
from page_parsing_one import get_first_links,get_all_data


def get_all_links_from(shell):
    for page in range(1,101):
        get_first_links(shell,page)


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from,list_url.split())
    pool.close()
    pool.join()
