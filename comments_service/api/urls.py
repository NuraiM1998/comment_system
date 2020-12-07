from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet


app_name='post_api'

router = DefaultRouter()

router.register('posts', PostViewSet, basename='post')


urlpatterns = [
    path('posts/<slug:slug>/comments/', 
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}), 
        name='post-comment-list'),
    path('posts/<slug:slug>/comments/<int:pk>/', 
        CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), 
        name='post-comment-detail'),
    path('posts/favorites/', PostViewSet.as_view({'get': 'favorite'}), 
        name='post_bookmark'),
    path('posts/favorites/add', PostViewSet.as_view({'post': 'add_to_favorite'}), 
        name='post_bookmark_add')
]

urlpatterns += router.urls
