# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.utils.project import get_project_settings

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article


class CoinDesk(CrawlSpider):
    name = '8btc'
    allowed_domains = ["8btc.com"]
    # todo 所有rule只为抽取页面列表，例如分页查询时的所有页面入口
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[@class='itm itm_new']/a"),
             callback='parse_content'),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='itm itm_new']/span/a[1]"),
             callback='link_parse'),

    )
    start_urls = ['http://www.8btc.com/sitemap?newPost=1']

    # 抽取出页面中的文章列表,调用parse_content抽取文章内容
    def link_parse(self, response):
        deeps = get_project_settings()['SPIDER_DEEP']
        links = response.xpath("//li[@class='itm itm_new']/a/@href").extract()
        for link in links:
            yield Request("http://www.8btc.com" + link, callback=self.parse_content)
        link_page = response.xpath("//li[@class='itm itm_new']/span/a/@href").extract()
        for page_item in link_page:
            page_id_list = page_item.split("pg=")
            print "detail", page_id_list[-1], deeps
            if len(page_id_list) == 2 and 1 < int(page_id_list[-1]) < deeps:
                yield Request("http://www.8btc.com" + page_item, callback=self.link_parse)

    # 根据文章页面的html，抽取文章内容
    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(
            response.xpath("//div[@class='article-title']/h1/text()").extract())
        content = CommonUtil.extractContent(response.xpath("//div[@class='article-content']"))
        item['content'] = content
        item['url'] = response.url
        item['domain'] = "http://www.8btc.com/"
        return item

