from django.contrib import admin
from App1.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'cteared_at')

admin.site.register(Book, BookAdmin)
