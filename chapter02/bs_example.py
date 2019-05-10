# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup

def scrape(html):
    soup = BeautifulSoup(html)
    tr = soup.find(attrs={'id':'places_area__row'}) # locate the area row
    # 'class' is a special python attribute so instead 'class_' is used
    td = tr.find(attrs={'class':'w2p_fw'})  # locate the area tag
    area = td.text  # extract the area contents from this tag
    return area

if __name__ == '__main__':
    html = request.urlopen('http://example.webscraping.com/places/default/view/Algeria-4').read()
    print(scrape(html))