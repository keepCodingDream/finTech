# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article


class Btc(CrawlSpider):
    name = 'btc123'
    allowed_domains = ["btc123.com"]
    start_urls = ('http://news.btc123.com/news/',)
    rules = (
        Rule(LinkExtractor(allow='/', restrict_xpaths="//div[@class='n_newscontent']/div[@class='n_newstitle']/a"),
             callback='parse_content'),

    )

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(response.xpath("//div[@class='n_dttile']/text()").extract())
        item['content'] = CommonUtil.extractContent(response.xpath("//div[@class='n_dtcont clearfloat']"))
        item['url'] = response.url
        item['domain'] = "http://www.btc123.com/"
        return item
