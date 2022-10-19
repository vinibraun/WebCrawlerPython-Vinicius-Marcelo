# import requests
# import re
#
# url = "https://www.tibiawiki.com.br/wiki/Itens"
# check = []
#
# r = requests.get(url)
# html = r.text.encode("utf8")
# search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html.decode("utf8"))
#
# for link in search:
#     if link not in search:
#         check.append(link)
#         with open("link.txt", "a") as file:
#             file.write(f'{link}\n')

# import scrapy
#
# class CrawlerBot(scrapy.Spider):
#     name="Whatssap 3"
#     start_urls = ["https://www.terabyteshop.com.br/perifericos"]
#
#     def _parse(self, response, **kwargs):
#         SELETOR = ".commerce_columns_item_image"
#         perifericos = []
#         for categoria in response.css(SELETOR):
#             periferico = {}
#
#             PRECO_SELETOR = ".prod-new-price"
#
#             periferico['preco'] = categoria.css(PRECO_SELETOR).extract_first()
#             print(periferico)
#
#             perifericos.append(periferico)


# import requests
# from bs4 import BeautifulSoup
# import html5lib
#
# URL = "https://www.tibiawiki.com.br/wiki/Itens"
# r = requests.get(URL)
# print(r.status_code)
#
# soup = BeautifulSoup(r.text, 'html.parser')
# #
# # with open("text.html", "w") as outfile:
# #     outfile.write(soup.pretiffy())
#
# tags = soup.find_all("a")
#
# for tag in tags:
#     print(tag)

import requests
from bs4 import BeautifulSoup
import lxml

# html = requests.get('https://www.tibiawiki.com.br/wiki/Itens').text
# soup = BeautifulSoup(html, 'lxml')
#
# for a_tag in soup.select('a[href*="/manga"]'):
#     link = a_tag['href']
#     link = link[1:]
#     print(f'https://www.tibiawiki.com.br/{link}')


import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)

if __name__ == '__main__':
    Crawler(urls=['https://www.imdb.com/']).run()