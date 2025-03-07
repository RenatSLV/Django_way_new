from django.shortcuts import render, redirect

from App1.models import Book
from App1.form import BookForm

def list_books(request):
    books = Book.objects.all()
    return render(request, 'list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = BookForm()
    return render(request, 'add.html', {'form': form})
