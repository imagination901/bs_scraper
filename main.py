from url_datamodel import UrlData
from bs4 import BeautifulSoup as bs
import requests
import sys
import html
import re
from prettytable import PrettyTable


arguments = sys.argv

urldata = UrlData()


def main():
    if len(arguments) > 1:

        url = arguments[1]
        urldata.url = url
        keyword = str(input("Please provide a keyword if you'd like to search for it: "))
        try:
            response = requests.get(url)
            html_object = html.unescape(response.text)
            soup = bs(html_object, 'html.parser')

            get_attributes(response)
            get_links(soup)

            if keyword:
                find_keywords(keyword, soup)
            
            print_table1()
            print_table2(urldata.extracted_links)
        except Exception as e:
            print("Ouch, this address doesn't respond.")


    else:
        print('Please provide the URL to scrape.')


def get_attributes(response):
    response = response 

    urldata.status_code = response.status_code
    urldata.elapsed_time = response.elapsed
    urldata.encoding = response.encoding


def get_links(soup):
    for link in soup.find_all('a'):
        urldata.extracted_links.append(link.get('href'))


def find_keywords(keyword, soup):
    soup_str = str(soup)
    matches = re.findall(f'{keyword}', soup_str, re.IGNORECASE)

    if len(matches) >= 1:
        urldata.contains_keyword = 'True'
        urldata.keyword_count = len(matches)
    else:
        urldata.contains_keyword = 'False'


def print_table1():
    table = PrettyTable()
    table.field_names = ['URL', 'Status Code', 'Encoding', 
                            'Elapsed Time', 'Contains Keyword', 'Keyword Count']
    table.add_row([urldata.url, urldata.status_code, urldata.encoding,
                    urldata.elapsed_time, urldata.contains_keyword, urldata.keyword_count])
    print(table) 


def print_table2(links):
    table = PrettyTable()
    table.field_names = ['#', 'Link']
    for i, link in enumerate(links, start=1):
        table.add_row([i, link])
    print(table)

if __name__ == "__main__":
    main()
