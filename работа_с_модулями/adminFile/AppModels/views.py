from django.shortcuts import render
from django.http import HttpResponse
from AppModels.models import *
from django.db.models import F


def get_data(request):
    news_list = News.objects.all()
    return render(request, 'index.html', {'news_list': news_list})

def new_list(request):
    queryset = News.objects.annotate(
        discount_price=F('price') / 2
    )
    return render(request, 'index2.html', {'queryset': queryset})
