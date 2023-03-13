from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    # Upload_Form,
    PostListView,
    PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    like_unlike_post
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='index'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create_post/', PostCreateView.as_view(), name='create-post'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('liked/', like_unlike_post, name='like-post-view'),
]
router = DefaultRouter(trailing_slash=True)

urlpatterns.extend(router.urls)
