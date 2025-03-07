from django.contrib import admin
from django.urls import path
from App1.views import Book_list_views_cl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Book_list_views_cl.as_view(), name='listBook')
]
