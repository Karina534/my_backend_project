from django.shortcuts import render
from .models import Articl

def news_home(request):
    news = Articl.objects.order_by('-data')
    return render(request, 'news/news_home.html', {'news': news})
