#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import ssl
from common.commonUtil import five_download

'''
在第一个简单的爬虫中，我们将使用示例网站robots.txt文件中发现的网站地图来下载所有网页。
为了解析网站地图，我们将会使用正则表达式，从<loc>标签中年提取出url
# section 1
User-agent: BadCrawler
Disallow: /

# section 2
User-agent: *
Disallow: /trap 
Crawl-delay: 5

# section 3
Sitemap: http://example.webscraping.com/sitemap.xml                                                                                                                                       
'''
def crawl_sitemap(url):
    # download the sitemap file
    sitemap = five_download(url,ssl._create_unverified_context())
    #python3 已经严格区分byte和str了。所以这里需要把byte转成str
    sitemapStr=sitemap.decode(encoding='utf-8');

    # extract the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemapStr)
    # download each link
    for link in links:
        html = five_download(link,ssl._create_unverified_context())
        # scrape html here
        # ...


if __name__ == '__main__':
    crawl_sitemap('http://example.webscraping.com/sitemap.xml')