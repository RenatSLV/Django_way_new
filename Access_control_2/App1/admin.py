from django.contrib import admin

from App1.models import Worker, Client, Coment

class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'experience', 'start_work']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'whouse_client']


class ComentAdmin(admin.ModelAdmin):
    list_display = ['content', 'content_type', 'object_id', 'content_object']


admin.site.register(Worker, WorkerAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Coment, ComentAdmin)
