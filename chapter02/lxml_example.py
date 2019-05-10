import lxml.html

from urllib import request

'''
遇到的问题，安装完lxml以后，还是需要按照cssselect的
'''
'''
选择所有标签：*
选择<a>标签 a
选择所有class="link"的元素：.link
选择class="link"的<a>标签：a.link
选择id="home"的<a>标签： a#home
选择父元素为<a>标签的所有<span>子标签:a>span
选择<a>标签内部的所有<span>标签 a span
选择title属性为"home"的所有<a>标签：a[title=Home]
'''
def scrape(html):
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]# locate the area row
    area = td.text_content()  # extract the area contents from this tag
    return area


if __name__ == '__main__':
    html = request.urlopen('http://example.webscraping.com/places/default/view/Algeria-4').read()
    print(scrape(html))