from django.contrib import admin
from App1.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_book', 'author', 'created_year', 'zhanr', 'created_at_post']

admin.site.register(Book, BookAdmin)
