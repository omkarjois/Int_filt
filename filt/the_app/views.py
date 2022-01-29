from django.shortcuts import render
from django.http import HttpResponse
from sys import path as syspath
syspath.append('/home/omkar/omkar/Int_filt/filt/the_app')
import amazon
import google_1 as g
# Create your views here.

query = "laptop"

def home(request):
    return render(request, 'home.html')

def search_page(request):
    a_list = amazon.search_amazon(query)
    f_list = []
    for i in a_list:
        u = g.convert_to_link(i.name)
        page_url = g.website_list(u)
        f_list.append(page_url)
        print(f_list)

    context = {
        'list' : amazon.search_amazon("laptop"),
        'f_list' : f_list
    }
    return render(request, 'search_page.html', context)