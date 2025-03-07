from django.contrib import admin
from django.urls import path
from App1.views import list_todos, add_todo, delete_todo, detail_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_todos, name='list'),
    path('add/', add_todo, name='add'),
    path('delete/<int:id>/', delete_todo, name='delete'),
    path('detail/<int:id>/', detail_todo, name='detail'),
]
