import requests
from bs4 import BeautifulSoup
from sys import path as syspath
syspath.append('..')

website_list = []
url = f'https://www.google.com/search?q=Acer+Aspire+3+AMD+Athlon+Silver+3050U+Dual-core+Processor+15.6%22+(39.6+cms)+Laptop+-+(4+GB%2F256+GB+SSD%2FWindows+11+Home%2FAMD+Radeon+Graphics+%2F1.9Kg%2FSilver)+A315-23&oq=Acer+Aspire+3+AMD+Athlon+Silver+3050U+Dual-core+Processor+15.6%22+(39.6+cms)+Laptop+-+(4+GB%2F256+GB+SSD%2FWindows+11+Home%2FAMD+Radeon+Graphics+%2F1.9Kg%2FSilver)+A315-23&aqs=chrome..69i57.689j0j7&sourceid=chrome&ie=UTF-8'

def convert_to_link(name):
    base_url = 'https://www.google.com/search?q='
    a = name.replace(' ', '+')
    b = a.replace('/', '%2')
    return base_url+b


def search_websites(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, features='lxml') 
    cards = soup.find_all('div', {'class': 'yuRUbf'})
    for i in cards:
        web = i.find('div', {'class': 'TbwUpd NJjxre'})
        if web.text[:24] == 'https://www.flipkart.com':
            a = i.find('a')
            l1 = str(a).split()
            for j in l1:
                if 'href' in j:
                    link = j[6:-1]
                    return link           
