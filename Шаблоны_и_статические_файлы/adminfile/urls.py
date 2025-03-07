from django.contrib import admin
from django.urls import path
from App1.views import list_Book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_Book_views, name='list'),
]
