from django.contrib import admin
from django.urls import path
from App1.views import CreatePost, Success

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Create/', CreatePost.as_view(), name='Create'),
    path('success/', Success.as_view(), name='success'),
]
