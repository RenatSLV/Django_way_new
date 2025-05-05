from django.contrib import admin
from django.urls import path
from App1.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test, name='name'),
]
