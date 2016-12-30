# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from webCrawler_scrapy.commonUtil import CommonUtil
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
        item['title'] = CommonUtil.delListEmpty(response.xpath('//header[@class="article-header"]/h1/text()').extract())
        item['content'] = CommonUtil.extractContent(response.xpath('//article[@class="article-content"]'))
        item['url'] = response.url
        item['domain'] = "http://www.bitcoin86.com/"
        return item
