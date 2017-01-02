# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule

from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article
from scrapy.utils.project import get_project_settings
from scrapy.http import Request

DOMAIN = 'http://www.bitecoin.com'


class Bitcoin(CrawlSpider):
    name = 'bitecoin'
    allowed_domains = ["bitecoin.com"]
    start_urls = (
        'http://www.bitecoin.com',
    )
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article/header/h1/a"),
             callback='parse_content'),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='nav-previous']/a"),
             callback='link_parse'),

    )

    # 分页信息抽取逻辑
    def link_parse(self, response):
        deeps = get_project_settings()['SPIDER_DEEP']
        # 不含有这种标签的就是实体文章
        links = response.xpath("//article/header/h1/a/@href").extract()
        if len(links) == 0:
            yield self.parse_content(response)
        else:
            for link_item in links:
                yield Request(link_item, callback=self.parse_content)
        # 抽取分页信息
        link_page = response.xpath("//div[@class='nav-previous']/a/@href").extract()
        print "link_page:", link_page
        for page_item in link_page:
            page_id_list = page_item.split("page/")
            this_page_list = response.url.split("page/")
            this_index = 1
            if len(this_page_list) == 2:
                this_index = this_page_list[-1]
            if len(page_id_list) == 2 and int(this_index) < int(page_id_list[-1]) < deeps:
                print page_item
                yield Request(this_index, callback=self.link_parse)

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(response.xpath('//article/header/h1/text()').extract())
        content = CommonUtil.delListEmpty(response.xpath('//article/div[@class="entry-content"]/text()').extract())
        item['content'] = content.join(
            CommonUtil.delListEmpty(response.xpath('//article/div[@class="entry-content"]/p/text()').extract()))
        item['url'] = response.url
        item['domain'] = "http://www.bitecoin.com/"
        return item
