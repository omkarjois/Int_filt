from sys import path as syspath
syspath.append('..')

from django.shortcuts import render
from django.http import HttpResponse
import amazon as a
# Create your views here.

def hello(request):
    return render(request, 'hello.html')

def search_page(request):
    context = {
        'list' : a.search_amazon("laptop")
    }
    return render(request, 'search_page.html', context)


