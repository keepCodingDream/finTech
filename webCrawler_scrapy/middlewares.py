#!/usr/bin/python
# -*- coding: utf-8 -*-
#

import random

from scrapy.conf import settings


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        ua = random.choice(self.agents)
        request.headers.setdefault('User-Agent', ua)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

#
