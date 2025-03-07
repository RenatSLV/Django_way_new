from django.contrib import admin
from django.urls import path
from App1.views import listUser, DetailUser, dontLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', listUser.as_view(), name='listUser'),
    path('detail/<int:user_id>', DetailUser.as_view(), name='DetailUser'),
    path('login/', dontLogin, name='dontLogin'),
]
