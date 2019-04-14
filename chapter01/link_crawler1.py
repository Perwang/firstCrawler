import re
import ssl
from common.commonUtil import five_download
"""http://www.runoob.com/python3/python3-reg-expressions.html#flags 正则表达式"""

def link_crawler(seed_url, link_regex):
    """Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url] # the queue of URL's to download
    while crawl_queue:
        url = crawl_queue.pop()
        html = five_download(url,ssl._create_unverified_context())
        # filter for links matching our regular expression
        for link in get_links(html):
            """
            书本里原来使用的是match，下面是match和search的区别
            re.match与re.search的区别re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
            """
            if re.search(link_regex, link,re.M|re.I):
                # add this link to the crawl queue
                crawl_queue.append(link)


def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com', 'index|view')