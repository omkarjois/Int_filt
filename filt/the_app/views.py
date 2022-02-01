from django.shortcuts import render
from django.http import HttpResponse
from sys import path as syspath
syspath.append('/home/omkar/omkar/Int_filt/filt/the_app')
import amazon
import google_1 as g
import flipkart
# Create your views here.

query = "laptop"

def home(request):
    return render(request, 'home.html')

def search_page(request):
    a_list = amazon.search_amazon(query)
    product_list = []
    for i in a_list:
        link = g.convert_to_link(i.name)
        print(link)
        f_link = g.search_websites(link)
        if f_link != None:
            f_details = flipkart.get_flipkart_details(f_link)
            prod = [i, f_details]
        else:
            prod = [i]
        product_list.append(prod)

    context = {
        'list' : product_list
        }
    return render(request, 'search_page.html', context)