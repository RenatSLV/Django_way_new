from django.contrib import admin
from django.urls import path
from App1.views import CreateUser, ListUsers, detailUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', CreateUser.as_view(), name='CreateUser'),
    path('list/', ListUsers.as_view(), name='ListUsers'),
    path('detail/', detailUser, name='DetailUser')
]
