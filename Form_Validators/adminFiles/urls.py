from django.contrib import admin
from django.urls import path
from App1.views import list_books, add_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_books, name='list_book'),
    path('add/', add_book, name='add_book'),
]
