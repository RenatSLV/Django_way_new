from django.contrib import admin
from django.urls import path
from ListTask.views import *

urlpatterns = [
    path('AllTask/', get_all, name='get_all'),
    path('Add/', add_task, name='add_task'),
    path('delete/', delet_task_by_id, name='Delete'),
    path('GetOne/', get_one_task_by_id, name='GetOne'),

]
