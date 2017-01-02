#!/bin/bash
export PATH=$PATH:/usr/local/bin
cd /home/core_staff/spider/finTech
git pull
wait
scrapy crawl bitbank &
scrapy crawl bitcoin86 &
scrapy crawl bitecoin scrapy crawl btc123 &
scrapy crawl coindesk &
scrapy crawl wabi &
scrapy crawl yuanbao &
scrapy crawl 8btc &





