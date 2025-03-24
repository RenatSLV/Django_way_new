from django.contrib import admin

from App1.models import User, User2
# Login: admin
# Password: 123

class UserAdmin(admin.ModelAdmin):
    list_display = ['owner', 'balance']


class User2Admin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age']


admin.site.register(User, UserAdmin)
admin.site.register(User2, User2Admin)
