from django.contrib import admin
from task_list.models import *
# renat 123
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'taskInfo', 'published')
    search_fields = ('task',)

admin.site.register(Task, TaskAdmin)