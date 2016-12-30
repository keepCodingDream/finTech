# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from webCrawler_scrapy.items import Article

class Bitcoin(Spider):
    name = 'bitcoin'
    allowed_domains = ["bitecoin.com"]
    start_urls = (
        'http://www.bitecoin.com',
    )

    def parse(self, response):
        item = Article()
        print "title" , response.xpath('//article/header/h1/a/@title').extract()
        print "herf" , response.xpath('//article/header/h1/a/@href').extract()
        print item
        return item
