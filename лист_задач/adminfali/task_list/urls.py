from django.contrib import admin
from django.urls import path, re_path
from task_list.views import *

urlpatterns = [
    re_path(r'^get_all/$', get_all, name='get_all'),
    re_path(r'^addTask/$', add_task, name='add_task'),
    re_path(r'^deleteTask/$', delet_task_by_id, name='delete_Task'),
]
