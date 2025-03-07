from django.contrib import admin
from django.urls import path
from firstapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('firstapp/', index)
]
