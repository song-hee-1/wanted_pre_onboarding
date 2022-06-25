from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('posts/', PostList, name='post_list'),
    path('posts/<int:pk>', PostDetail, name='post_detail'),
]
