from django.urls import path
from worksApi.views import *

urlpatterns = [
    path('data/', WorkAPI, name='WorkAPI'),
    path('index/', index, name='index'),
    path('main/', main, name='main'),
    path('list/', lists, name='lists'),
    path('card/', card, name='card'),
]