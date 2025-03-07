from django.contrib import admin
from django.urls import path
from App1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index2/', index2, name='index2'),
]
