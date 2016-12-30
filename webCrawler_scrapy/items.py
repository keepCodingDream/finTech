#!/usr/bin/python
# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    '''定义需要格式化的内容（或是需要保存到数据库的字段）'''
    domain = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    created = scrapy.Field()
    content = scrapy.Field()
