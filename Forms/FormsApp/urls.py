from django.contrib import admin
from django.urls import path
from FormsApp.views import listIceCream, addIceCream

urlpatterns = [
    path('', listIceCream, name='list'),
    path('add/', addIceCream, name='add'),
]