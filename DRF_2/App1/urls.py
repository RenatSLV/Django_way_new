from django.urls import path
from .views import create_note, register_user

urlpatterns = [
    path('note/', create_note, name='create-note'),
    path('register/', register_user, name='register'),
]
