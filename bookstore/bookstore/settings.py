# -*- coding: utf-8 -*-

# Scrapy settings for bookstore project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bookstore'

SPIDER_MODULES = ['bookstore.spiders']
NEWSPIDER_MODULE = 'bookstore.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'bookstore.middlewares.BookstoreSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'bookstore.pipelines.BookstorePipeline': 300,
    'bookstore.pipelines_mysql.MYSQLPIPELINE': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# ----------------- Mysql配置 ------------------------#
MYSQL_SETTINGS = {
    'HOST': '127.0.0.1',  # 数据库地址
    'DATABASE': 'book_store',  # 数据库名称
    'USER': 'root',  # 登陆用户名
    'PASSWORD': 'wwwwwwww1',  # 登陆密码
    'CHARSET': 'utf8'

}
SPIDER_DB_OP_DISPACH = {'bs': {
    'Classify_Item': ('insert into classify(classify_id,classify_name) VALUES (%s,%s)', ('classify_id', 'classify_name')),

    'Book_Item': ('insert into book(classify_id,book_id,img_url,book_name,writer,miaoshu) VALUES (%s,%s,%s,%s,%s,%s)',
                   ('classify_id', 'book_id', 'img_url', 'book_name', 'writer', 'miaoshu',)),
    'BookDetail_Item': ('insert into bookdetail(zhangjie,text,book_id) VALUES (%s,%s,%s)', ('zhangjie', 'text', 'book_id')),

}
}
LOG_LEVEL = "DEBUG"

from datetime import datetime
import os

today = datetime.now()

LOG_DIR = "log"
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_FILE = "{}/scrapy_{}_{}_{}.log".format(LOG_DIR, today.year, today.month, today.day)
