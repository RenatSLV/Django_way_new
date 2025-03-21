from django.contrib import admin
from django.urls import path

from App1.views import list_coments
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_coments, name='list_coments'),
]
