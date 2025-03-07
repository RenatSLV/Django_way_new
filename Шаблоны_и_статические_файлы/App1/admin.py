from django.contrib import admin
from App1.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'year', 'cost']

admin.site.register(Book, BookAdmin)