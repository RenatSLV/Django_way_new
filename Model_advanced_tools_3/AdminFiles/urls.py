from django.contrib import admin
from django.urls import path

from App1.views import list_user, transfer_money

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_user, name='list_user'),
    path('transfer/', transfer_money, name='transfer_money'),
]
