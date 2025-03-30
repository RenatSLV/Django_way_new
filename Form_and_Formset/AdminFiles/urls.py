from django.contrib import admin
from django.urls import path, include

from App1.views import add_Client, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add/', add_Client, name='add_Client'),
]

urlpatterns += [
    path('captcha/', include('captcha.urls')),
]