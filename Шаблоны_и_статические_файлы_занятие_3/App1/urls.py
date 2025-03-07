from django.contrib import admin
from django.urls import path
from App1.views import base_views

urlpatterns = [
    path('', base_views, name='home')
]
