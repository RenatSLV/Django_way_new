from django.urls import path
from App1.views import PostListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
]
