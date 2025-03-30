from django.contrib import admin

from App1.models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']

admin.site.register(Client, ClientAdmin)
