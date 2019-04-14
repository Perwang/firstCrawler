# -*- coding: utf-8 -*-


import itertools
from commonUtil import five_download
import ssl

def iteration():
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-{}'.format(page)
        html = five_download(url,ssl._create_unverified_context())
        if html is None:
            # received an error trying to download this webpage
            # so assume have reached the last country ID and can stop downloading
            break
        else:
            # success - can scrape the result
            # ...
            pass


if __name__ == '__main__':
    iteration()