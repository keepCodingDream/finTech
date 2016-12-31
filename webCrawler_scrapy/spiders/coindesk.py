# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.utils.project import get_project_settings

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article


class CoinDesk(CrawlSpider):
    name = 'coindesk'
    allowed_domains = ["coindesk.com"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[contains(@class,'article')]/div[@class='picture']/a"),
             callback='parse_content'),

    )

    def __new__(cls, *args, **kwargs):
        start_list = ['http://www.coindesk.com/category/news/']
        i = 2
        deeps = get_project_settings()['SPIDER_DEEP']
        while i < deeps:
            start_list.append('http://www.coindesk.com/category/news/page/' + bytes(i) + "/")
            i += 1
        CoinDesk.start_urls = start_list
        print CoinDesk.start_urls
        return super(CoinDesk, cls).__new__(cls, *args, **kwargs)

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(response.xpath("//div[@class='single-title']/h1/text()").extract())
        content = CommonUtil.delListEmpty(response.xpath("//div[@class='single-content']/p/text()").extract())
        item['content'] = content
        item['url'] = response.url
        item['domain'] = "http://www.coindesk.com/"
        return item
