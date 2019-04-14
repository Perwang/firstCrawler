# -*- coding: utf-8 -*-

from urllib import request
import re


def scrape(html):
    area = re.findall('<tr id="places_area__row">.*?<td\s*class=["\']w2p_fw["\']>(.*?)</td>', html)[0]
    return area


if __name__ == '__main__':
    html = request.urlopen('http://example.webscraping.com/places/default/view/Aland-Islands-2').read()
    print(scrape(html.decode(encoding='utf-8')))