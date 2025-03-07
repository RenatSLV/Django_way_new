from django.contrib import admin
from django.urls import path

from App1.views import listUsers, addUser
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listUsers, name='listUser'),
    path('add/', addUser, name='addUser'),
]
