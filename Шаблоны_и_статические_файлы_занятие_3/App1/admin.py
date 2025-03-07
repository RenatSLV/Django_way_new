from django.contrib import admin
from App1.models import Film

class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'zhanr', 'year', 'country', 'view', 'created_at']

admin.site.register(Film, FilmAdmin)