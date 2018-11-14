# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from scrapy.http import Request

# from scrapy.spiders import CrawlSpider


from bookstore.items import Classify_Item, Book_Item, BookDetail_Item


class BsSpider(scrapy.Spider):
    name = 'bs'
    allowed_domains = ['www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com']

    def parse(self, response):
        ul1 = response.xpath("//ul[@class='channel-nav-list']/li")
        for li in ul1:
            fen_lei = li.xpath("./a/text()").extract_first()
            feilei_url = li.xpath("./a/@href").extract_first()
            classify_id = int(re.findall(r'\d+', feilei_url)[0])
            item = Classify_Item(classify_name=fen_lei, classify_id=classify_id)
            yield item
            req = Request(url=feilei_url, meta={'data': classify_id}, callback=self.zhongzhuan)
            yield req

    def zhongzhuan(self, response):
        ul2 = response.xpath("//ul[@class='seeWell cf']/li")[0:30]
        classify_id = int(response.meta['data'])
        for li2 in ul2:
            surl = li2.xpath("./span[@class='l']/a[@class='clearfix stitle']/@href").extract_first()
            req = Request(url=surl, meta={'data': classify_id}, callback=self.two)
            yield req

    def two(self, response):
        classify_id = int(response.meta['data'])
        qurl = response.xpath("//div[@class='b-oper']/a[@class='reader']/@href").extract_first()
        book_id = int(re.findall(r'\d+$', qurl)[0])
        book_name = response.xpath("//div[@class='b-info']/h1/text()").extract_first()
        img_url = response.xpath("//div[@class='detail']/a[@class='l mr11']/img/@src").extract_first()
        writer = response.xpath("//dl[@class='bookso'][1]/dd/text()").extract_first()
        miaoshu = response.xpath("//div[@id='waa']/text()").extract_first()
        item = Book_Item(img_url=img_url, book_name=book_name, writer=writer, miaoshu=miaoshu, classify_id=classify_id,
                         book_id=book_id)
        yield item
        req = Request(url=qurl, meta={'data': book_id}, callback=self.three)
        yield req

    def three(self, response):
        ul3 = response.xpath("//div[@class='chapterNum']/ul/div[@class='clearfix dirconone']/li")[0:20]
        for li in ul3:
            zhangjie = li.xpath("./a/text()").extract_first()
            text = li.xpath("./a/@href").extract_first()
            book_id = int(response.meta['data'])
            item = BookDetail_Item(zhangjie=zhangjie, text=text, book_id=book_id)
            yield item
