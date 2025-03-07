from django.shortcuts import render
from App1.models import Book

def list_Book_views(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'base.html', context)
