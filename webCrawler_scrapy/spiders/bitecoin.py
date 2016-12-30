# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article


class Bitcoin(CrawlSpider):
    name = 'bitecoin'
    allowed_domains = ["bitecoin.com"]
    start_urls = (
        'http://www.bitecoin.com',
    )
    rules = (
        Rule(LinkExtractor(allow='/', restrict_xpaths='//article/header/h1/a'),
             callback='parse_content'),

    )

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(response.xpath('//article/header/h1/text()').extract())
        content = CommonUtil.delListEmpty(response.xpath('//article/div[@class="entry-content"]/text()').extract())
        item['content'] = content.join(
            CommonUtil.delListEmpty(response.xpath('//article/div[@class="entry-content"]/p/text()').extract()))
        item['url'] = response.url
        item['domain'] = "http://www.bitecoin.com/"
        return item
