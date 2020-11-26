from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('post/create/', PostCreateAPIView.as_view(), name='postapi_create')
]

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('comments', CommentViewSet, basename='comment')
urlpatterns = [
    path('', include(router.urls)),
    path('posts/<slug:slug>/comments/', CommentViewSet.as_view({'get': 'list'}), name='post-comment-list'),
    path('posts/<slug:slug>/comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve'}), name='post-comment-detail')
]
