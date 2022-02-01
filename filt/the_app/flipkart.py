import requests
from bs4 import BeautifulSoup
from sys import path as syspath
syspath.append('..')
from models import Product, Review

url = 'https://www.flipkart.com/hp-pavilion-ryzen-5-hexa-core-5600h-8-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-144-hz-15-ec2004ax-gaming-laptop/p/itm98c94bbf9bc20'

flipkart_product_list = []

def get_flipkart_details(url):
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
        }
        response = requests.get(url, headers=headers).text
        soup = BeautifulSoup(response, features='lxml')
        cards = soup.find_all('div', {'class' : '_1YokD2 _3Mn1Gg col-8-12'})
        for i in cards:
            product = Product('flipkart')
            #name
            product.name = i.find('span', {'class' : 'B_NuCI'}).text
            #price
            product.price = i.find('div', {'class' : '_30jeq3 _16Jk6d'}).text
            #url
            product.url = url
            flipkart_product_list.append(product)
            return product

