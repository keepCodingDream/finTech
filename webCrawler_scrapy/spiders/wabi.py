# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.utils.project import get_project_settings

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article

DOMAIN = "https://www.wabi.com/"


class Wabi(CrawlSpider):
    name = 'wabi'
    allowed_domains = ["wabi.com"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[@class='pbox clr']/div[@class='word']/a"),
             callback='parse_content'),
        Rule(LinkExtractor(restrict_xpaths="//div[contains(@class,'pages')]/a"),
             callback='link_parse'),

    )
    start_urls = ['https://www.wabi.com/news/all/page_1.html']

    # 分页信息抽取逻辑
    def link_parse(self, response):
        deeps = get_project_settings()['SPIDER_DEEP']
        # 首先判断是不是文章页面
        links = response.xpath("//li[@class='pbox clr']/div[@class='word']/a/@href").extract()
        print "links", links
        if len(links) > 0:
            for link in links:
                yield Request(DOMAIN + link, callback=self.parse_content)
        page_url = response.url
        page_size = page_url.split("page_")
        # 如果是size=2，就是分页页面
        if len(page_size) == 2:
            page_index = page_url.split("page_")[1].replace('.html', '')
            if 1 < int(page_index) < deeps:
                print page_url
                yield Request(page_url, callback=self.link_parse)

    # 具体的文章抽取逻辑
    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(
            response.xpath("//div[@class='pageTop']/h1/text()").extract())
        content = CommonUtil.extractContent(response.xpath("//div[contains(@class,'pageCont')]"))
        item['content'] = content
        item['url'] = response.url
        item['domain'] = DOMAIN
        return item
