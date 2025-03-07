from django.contrib import admin
from django.urls import path

from Access_controlApp.views import ListUserView, CreateGroupView, CreateUserView, LogInView, LogOutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListUserView, name='list_user'),
    path('createGroup/', CreateGroupView, name='create_group'),
    path('createUser/', CreateUserView, name='create_user'),
    path('LogIn/', LogInView, name='LogIn'),
    path('LogOut/', LogOutView, name='LogOut'),
]
