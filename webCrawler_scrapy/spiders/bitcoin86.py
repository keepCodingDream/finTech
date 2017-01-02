# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article
from scrapy.utils.project import get_project_settings
from scrapy.http import Request

DOMAIN = 'http://www.bitcoin86.com'


class Bitcoin86(CrawlSpider):
    name = "bitcoin86"
    allowed_domains = ["bitcoin86.com"]
    start_urls = (
        'http://www.bitcoin86.com/bitcoin/',
    )

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//article/a'),
             callback='parse_content'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="widget widget_ui_posts"]/ul/li/a'),
             callback='parse_content'),
        Rule(LinkExtractor(restrict_xpaths='//div[@class="pagination"]/ul/li/a'),
             callback='link_parse'),

    )

    # 分页信息抽取逻辑
    def link_parse(self, response):
        deeps = get_project_settings()['SPIDER_DEEP']
        # 不含有这种标签的就是实体文章
        links = response.xpath("//article/a/@href").extract()
        if len(links) == 0:
            yield self.parse_content(response)
        else:
            for link_item in links:
                yield Request(DOMAIN + link_item, callback=self.parse_content)
        # 抽取分页信息
        link_page = response.xpath("//div[@class='pagination']/ul/li/a/@href").extract()
        print "link_page:", link_page
        for page_item in link_page:
            page_id_list = page_item.split("_")
            this_page_list = response.url.split("_")
            this_index = 1
            if len(this_page_list) == 3:
                this_index = this_page_list[-1].replace('.html', '')
            if len(page_id_list) == 3 and int(this_index) < int(page_id_list[-1].replace('.html', '')) < deeps:
                print page_item
                yield Request(DOMAIN + page_item, callback=self.link_parse)

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(response.xpath('//header[@class="article-header"]/h1/text()').extract())
        item['content'] = CommonUtil.extractContent(response.xpath('//article[@class="article-content"]'))
        item['url'] = response.url
        item['domain'] = "http://www.bitcoin86.com/"
        return item
