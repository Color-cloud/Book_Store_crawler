# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Classify_Item(scrapy.Item):
    classify_id = scrapy.Field()
    classify_name = scrapy.Field()

    def get_name(self):
        return Classify_Item.__name__


class Book_Item(scrapy.Item):
    classify_id = scrapy.Field()
    book_id = scrapy.Field()
    img_url = scrapy.Field()
    book_name = scrapy.Field()
    writer = scrapy.Field()
    miaoshu = scrapy.Field()

    def get_name(self):
        return Book_Item.__name__


class BookDetail_Item(scrapy.Item):
    book_id = scrapy.Field()
    zhangjie = scrapy.Field()
    text = scrapy.Field()

    def get_name(self):
        return BookDetail_Item.__name__
