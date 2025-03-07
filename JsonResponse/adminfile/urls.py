from django.contrib import admin
from django.urls import path
from JsonResponse.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Json/', jsonresponse, name='jsonresponse'),
    path('redirect/', redirectfunc, name='redirect'),
    path('index/', index, name='index'),
    path('GetMethod/', GetMethod, name='getmethod'),
]
