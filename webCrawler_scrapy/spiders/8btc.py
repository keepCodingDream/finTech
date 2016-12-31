# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article
from scrapy.utils.project import get_project_settings


class CoinDesk(CrawlSpider):
    name = '8btc'
    allowed_domains = ["8btc.com"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[@class='itm itm_new']/a"),
             callback='parse_content'),

    )

    def __new__(cls, *args, **kwargs):
        i = 2
        deeps = get_project_settings()['SPIDER_DEEP']
        start_list = ['http://www.8btc.com/sitemap?newPost=1']
        while i < deeps:
            start_list.append('http://www.8btc.com/sitemap?newPost=1&pg=' + bytes(i) + "/")
            i += 1
        CoinDesk.start_urls = start_list
        return super(CoinDesk, cls).__new__(cls, *args, **kwargs)

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(
            response.xpath("//div[@class='article-title']/h1/text()").extract())
        content = CommonUtil.extractContent(response.xpath("//div[@class='article-content']"))
        item['content'] = content
        item['url'] = response.url
        item['domain'] = "http://www.8btc.com/"
        return item
