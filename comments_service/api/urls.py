from django.urls import path, include
from .views import PostViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('post/create/', PostCreateAPIView.as_view(), name='postapi_create')
]

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
urlpatterns = [
    path('', include(router.urls)),
]
