from django.urls import path
from .views import PostList, PostDetail, ApplyPost

urlpatterns = [
    path('posts/', PostList, name='post_list'),
    path('posts/<int:pk>', PostDetail, name='post_detail'),
    path('posts/<int:pk>/apply', ApplyPost, name='apply_post')
]
