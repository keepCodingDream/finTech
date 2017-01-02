# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.utils.project import get_project_settings
from webCrawler_scrapy.commonUtil import CommonUtil
from webCrawler_scrapy.items import Article
from scrapy.http import Request

DOMAIN = 'https://www.yuanbao.com'


# 该站点新闻都是别的网站新闻，只爬取他们自己项目相关信息
class Yuanbao(CrawlSpider):
    name = 'yuanbao'
    allowed_domains = ["yuanbao.com"]
    start_urls = ['https://www.yuanbao.com/news/?corpid=1']
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='page_a']"),
             callback='link_parse'),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='hideli']/a[1]"),
             callback='parse_content'),

    )

    # 分页信息抽取逻辑
    def link_parse(self, response):
        deeps = get_project_settings()['SPIDER_DEEP']
        # 不含有这种标签的就是实体文章
        links = response.xpath("//li[@class='hideli']/a/@href").extract()
        if len(links) == 0:
            yield self.parse_content(response)
        else:
            for link_item in links:
                yield Request(DOMAIN + link_item, callback=self.parse_content)
        # 抽取分页信息
        link_page = response.xpath("//a[@class='page_a']/@href").extract()
        print "link_page:", link_page
        for page_item in link_page:
            page_id_list = page_item.split("&p=")
            this_page_list = response.url.split("&p=")
            this_index = 1
            if len(this_page_list) == 2:
                this_index = this_page_list[-1]
            if len(page_id_list) == 2 and int(this_index) < int(page_id_list[-1]) < deeps:
                print page_item
                yield Request(DOMAIN + "/news" + page_item, callback=self.link_parse)

    def parse_content(self, response):
        item = Article()
        item['title'] = CommonUtil.delListEmpty(
            response.xpath("//div[@class='product left clearfix']/div[1]/h2/text()").extract())
        item['content'] = CommonUtil.extractContent(response.xpath("//div[@class='paragraph paragraph_news']"))
        item['url'] = response.url
        item['domain'] = DOMAIN
        return item
