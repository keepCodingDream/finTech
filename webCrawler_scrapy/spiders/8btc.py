# -*- coding: utf-8 -*-
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.utils.project import get_project_settings

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article

DOMAIN = "http://www.8btc.com/"


class CoinDesk(CrawlSpider):
    name = '8btc'
    allowed_domains = ["8btc.com"]
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//li[@class='itm itm_new']/a"),
             callback='parse_content'),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='itm itm_new']/span/a"),
             callback='link_parse'),

    )
    start_urls = ['http://www.8btc.com/sitemap?newPost=1']

    # 分页信息抽取逻辑
    def link_parse(self, response):
        deeps = get_project_settings()['SPIDER_DEEP']
        # 不含有这种标签的就是实体文章
        links = response.xpath("//li[@class='itm itm_new']/a/@href").extract()
        if len(links) == 0:
            yield self.parse_content(response)
        else:
            for link_item in links:
                yield Request(DOMAIN + link_item, callback=self.parse_content)
        # 抽取分页信息
        link_page = response.xpath("//li[@class='itm itm_new']/span/a/@href").extract()
        print "link_page:", link_page
        for page_item in link_page:
            page_id_list = page_item.split("pg=")
            this_page_list = response.url.split("pg=")
            this_index = 1
            if len(this_page_list) == 2:
                this_index = this_page_list[-1]
            if len(page_id_list) == 2 and int(this_index) < int(page_id_list[-1]) < deeps:
                print page_item
                yield Request(page_item, callback=self.link_parse)

    # 具体的文章抽取逻辑
    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(
            response.xpath("//div[@class='article-title']/h1/text()").extract())
        content = CommonUtil.extractContent(response.xpath("//div[@class='article-content']"))
        item['content'] = content
        item['url'] = response.url
        item['domain'] = DOMAIN
        return item
