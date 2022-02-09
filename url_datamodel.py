from dataclasses import dataclass


@dataclass
class UrlData:
    '''Class for keeping track of the scraped data from the URL'''
    url = ''
    status_code = ''
    encoding = ''
    elapsed_time = ''
    contains_keyword = 'No keyword provided'
    keyword_count = 0
    extracted_links = []

