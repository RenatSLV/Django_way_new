from django.contrib import admin
from ListTask.models import *
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'Task', 'Task_Info', 'published')
    search_fields = ('Task',)

admin.site.register(Task, TaskAdmin)
