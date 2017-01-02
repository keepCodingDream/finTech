#!/bin/bash
export PATH=$PATH:/usr/local/bin
cd /home/core_staff/spider/finTech
echo "hello world-tracy" >> /home/core_staff/file.txt
git pull
scrapy crawl bitbank
scrapy crawl bitcoin86




