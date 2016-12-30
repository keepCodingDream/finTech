# -*- coding: utf-8 -*-
from scrapy import log
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from webCrawler_scrapy.items import Article


class Bitcoin86(CrawlSpider):
    name = "bitcoin86"
    allowed_domains = ["bitcoin86.com"]
    start_urls = (
        'http://www.bitcoin86.com/',
    )

    rules = (
        Rule(LinkExtractor(allow='/', restrict_xpaths='//article/a'),
             callback='parse_content'),

    )

    def parse_content(self, response):
        item = Article()
        item['title'] = self.delListEmpty(response.xpath('//header[@class="article-header"]/h1/text()').extract())
        content = self.delListEmpty(response.xpath('//article[@class="article-content"]/text()').extract())
        item['content'] = content.join(
            self.delListEmpty(response.xpath('//article[@class="article-content"]/p/text()').extract()))
        item['url'] = response.url
        item['domain'] = "http://www.bitcoin86.com/"
        return item

    def delListEmpty(self, ori_list):
        result = ''
        for item in ori_list:
            if item is not None:
                result += item.strip()
        return result
