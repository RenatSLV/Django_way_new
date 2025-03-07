from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from App1.models import Book

class Book_list_views_cl(ListView):
    model = Book
    template_name = 'list.html'
    context_object_name = 'books'
    paginate_by = 5
    
