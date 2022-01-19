from sys import path as syspath
syspath.append('..')
from models import Product, RELIANCE_SOURCE
import requests
from bs4 import BeautifulSoup

root = 'https://www.reliancedigital.in'

def _query_to_url(query):
    url = f'https://www.reliancedigital.in/search?q={query}:relevance'
    return url

def search_reliance(query):
	url = _query_to_url(query)
	html_text = requests.get(url).text

	soup = BeautifulSoup(html_text, 'lxml')
	cards = soup.find_all('li', class_ =
		'grid pl__container__sp blk__lg__3 blk__md__4 blk__sm__6 blk__xs__6')

	products = []
	for li in cards:
		product_a = li.div.a

		product = Product(RELIANCE_SOURCE)

		product.url = root+product_a.get('href')

		product.name  = product_a.find('p', class_ = 'sp__name').text
		product.price = product_a.find('span', class_ = 'sc-bxivhb dmBTBc').text

		image_div = product_a.find('img', class_ = 'img-responsive imgCenter')
		product.imgurl = root+image_div.get('data-srcset')

		products.append(product)

	return products


print(search_reliance(_query_to_url('phone')))
