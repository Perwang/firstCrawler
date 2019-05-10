import lxml.html

from urllib import request

def scrape(html):
    tree = lxml.html.fromstring(html)
    td = tree.cssselect('tr#places_area__row > td.w2p_fw')[0]# locate the area row
    area = td.text_content()  # extract the area contents from this tag
    return area


if __name__ == '__main__':
    html = request.urlopen('http://example.webscraping.com/places/default/view/Algeria-4').read()
    print(scrape(html))