# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from webCrawler_scrapy.items import Article
from scrapy.linkextractors import LinkExtractor


class Forbes(CrawlSpider):
    name = "forbes"
    allowed_domains = ["www.forbes.com"]
    start_urls = (
        'www.forbes.com/most-popular/#4dbdd06828c7',
    )

    rules = (
        Rule(LinkExtractor(allow='/tag/哲学',restrict_xpaths=('//*[@id="subject_list"]/div[2]/span/a')),
             callback='link_parse',follow=True),

    )

    def link_parse(self, response):
        links = response.css('div.info > h2 > a::attr(href)').extract()
        for link in links:
            yield Request(link,callback=self.parse_content)

    def parse_content(self, response):
        item = Article()
        item['title'] = response.xpath('//*[@id="wrapper"]/h1/span/text()').extract()
        item['author'] = response.css('div#info > span >a::text').extract_first()
        # item['pub_date'] = response.xpath('//*[@id="info"]/text()[4]').extract()
        # item['price'] =response.xpath('//*[@id="info"]/text()[6]').extract()
        item['desc'] = response.xpath('//*[@id="link-report"]/div[1]/div/p').extract_first() or \
                        response.xpath('//*[@id="link-report"]/span[1]/div/p').extract_first()
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        return item


