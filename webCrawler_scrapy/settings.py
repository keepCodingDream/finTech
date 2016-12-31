# -*- coding: utf-8 -*-

BOT_NAME = 'webCrawler_scrapy'  # 与自己实现的爬虫类中的name属性一致

SPIDER_MODULES = ['webCrawler_scrapy.spiders']
NEWSPIDER_MODULE = 'webCrawler_scrapy.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

DEFAULT_REQUEST_HEADERS = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q = 0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
}
ROBOTSTXT_OBEY = True

# 下载延迟2s
DOWNLOAD_DELAY = 2

# 下载器
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'webCrawler_scrapy.middlewares.RandomUserAgent': 420,
}

# pilline的保存方式
ITEM_PIPELINES = {
    'webCrawler_scrapy.pipelines.JsonWithEncodingPipeline': 1000,  # 保存到文件中
    'webCrawler_scrapy.pipelines.WebcrawlerScrapyPipeline': 1000,  # 保存到mysql数据库
}

# 随机的USER_AGENTS池
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# 一些通用配置
# 关闭重定向
REDIRECT_ENABLED = False
# 减小下载超时
DOWNLOAD_TIMEOUT = 15
# 禁止重试
RETRY_ENABLED = False
# 禁用cokies
COOKIES_ENABLED = True

LOG_LEVEL = 'INFO'
# 全局并发
CONCURRENT_REQUESTS = 2000

# Mysql数据库的配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'testdb'  # 数据库名字，请修改
MYSQL_USER = 'root'  # 数据库账号，请修改
MYSQL_PASSWD = 'root'  # 数据库密码，请修改

MYSQL_PORT = 3306  # 数据库端口，在dbhelper中使用

# 业务深度
SPIDER_DEEP = 10
# 爬虫深度
DEPTH_LIMIT = 10
