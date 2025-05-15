from django.urls import path
from .views import RegisterView, HelloView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # доступен всем
    path('hello/', HelloView.as_view(), name='hello'),           # только с токеном
]
