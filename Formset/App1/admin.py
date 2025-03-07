from django.contrib import admin

from App1.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'created_at')

admin.site.register(User, UserAdmin)
