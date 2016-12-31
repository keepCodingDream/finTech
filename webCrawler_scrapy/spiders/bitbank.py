# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.utils.project import get_project_settings

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article


class CoinDesk(CrawlSpider):
    name = 'bitbank'
    allowed_domains = ["bitbank.com"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='item clearfix']/a"),
             callback='parse_content'),

    )

    def __new__(cls, *args, **kwargs):
        deeps = get_project_settings()['SPIDER_DEEP']
        start_list = ['https://www.bitbank.com/news']
        # 此处是抽取所有分页列表的请求地址数组
        i = 2
        while i < deeps:
            start_list.append('https://www.bitbank.com/news?page=' + bytes(i) + "/")
            i += 1
        CoinDesk.start_urls = start_list
        print CoinDesk.start_urls
        return super(CoinDesk, cls).__new__(cls, *args, **kwargs)

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(
            response.xpath("//div[@class='bk-newsContain']/div[@class='hd']/h2/text()").extract())
        content = CommonUtil.extractContent(response.xpath("//div[@class='bk-newsContain']/div[@class='bd']"))
        item['content'] = content
        item['url'] = response.url
        item['domain'] = "http://www.bitbank.com/"
        return item
