# -*- coding: utf-8 -*-


import itertools
from commonUtil import five_download
import ssl



def iteration():
    max_errors = 5 # maximum number of consecutive download errors allowed
    num_errors = 0 # current number of consecutive download errors
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/places/default/view/-{}'.format(page)
        html = five_download(url,ssl._create_unverified_context())
        if html is None:
            # received an error trying to download this webpage
            num_errors += 1
            if num_errors == max_errors:
                # reached maximum amount of errors in a row so exit
                break
            # so assume have reached the last country ID and can stop downloading
        else:
            # success - can scrape the result
            # ...
            num_errors = 0


if __name__ == '__main__':
    iteration()