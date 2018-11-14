# -*- coding: utf-8 -*-  
__author__ = 'zhougy'
__date__ = '2018/10/20 下午9:04'

import os, sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # 当前main.py的文件夹路径

SPIDER_NAME = "bs"  # 此名称是我们采用 scrapy genspider  spider_name 指定的spider_name

execute(["scrapy", "crawl", SPIDER_NAME])
