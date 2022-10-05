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

html = requests.get('https://www.tibiawiki.com.br/wiki/Itens').text
soup = BeautifulSoup(html, 'lxml')

for a_tag in soup.select('a[href*="/manga"]'):
    link = a_tag['href']
    link = link[1:]
    print(f'https://www.tibiawiki.com.br/{link}')