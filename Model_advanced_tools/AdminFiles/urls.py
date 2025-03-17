from django.contrib import admin
from django.urls import path

from App1.views import list_Students_Course

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_Students_Course, name='list_Students_Course'),
]
