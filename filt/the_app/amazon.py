import requests
from bs4 import BeautifulSoup
from sys import path as syspath
syspath.append('..')
from models import Product, Review, AMAZON_SOURCE

review_list = []

amazon_product_url = 'https://www.amazon.in/dp/'

def _query_to_url(query):
    url = f'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords={query}'
    return url


def search_amazon(query):
    url = _query_to_url(query)
    global a_product_list
    a_product_list = []
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, features='lxml')

    products = []
    cards = soup.find_all('div', {'data-component-type':'s-search-result'})
    for div in cards:
        product = Product(AMAZON_SOURCE)

        product.name = div.find('span', {'class':'a-size-medium a-color-base a-text-normal'}).text
        #'class':'a-size-base a-color-base a-text-normal', 'class':'a-size-base-plus a-color-base a-text-normal'}))

        image = str(div.find('img', {'class':'s-image'}))
        image_tag = image.split()
        for j in image_tag:
            if 'src=' in j: break
        product.imgurl = j[5:-1]

        price_tag = div.find('span', {'class':'a-offscreen'})
        product.price = price_tag

        data_asin = str(div).split()
        for j in data_asin:
            if "data-asin" in j:
                len1 = len(j)
                link = amazon_product_url+j[11:len1-1]
                product.url = link

        a_product_list.append(product)
    return a_product_list


def get_amazon_reviews(url):
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
        response = requests.get(url, headers=headers).text
        soup = BeautifulSoup(response, features='lxml')

        reviews = soup.find_all('div', {'data-hook':'review'})

        for i in reviews:
            #username
            username = i.find('span', {'class' : 'a-profile-name'}).text
            #print(username)

            #product
            prod = i.find('span', {'id' : 'productTitle'})
            #print(prod)

            #stars
            stars = i.find('span', {'class' : 'a-icon-alt'}).text
            #print(stars)

            #title
            title = i.find('a', {'data-hook' : 'review-title'}).text
            #print(title)

            date = i.find('span', {'data-hook' : 'review-date'}).text
            #print(date)

            text = i.find('div', {'data-hook' : 'review-collapsed'}).text
            #print(text)

            upvotes = i.find('span', {'data-hook' : 'helpful-vote-statement'}).text
            #print(upvotes)

            rev = Review(prod)
            rev.date = date
            rev.title = title
            rev.stars = stars
            rev.review = text
            rev.reviewer = username
            rev.upvotes = upvotes
            review_list.append(rev)

print(search_amazon('laptop'))