from django.contrib import admin
from FormsApp.models import IceCream

class IceCreamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'create_at']

admin.site.register(IceCream, IceCreamAdmin)