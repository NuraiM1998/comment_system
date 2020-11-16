''' Пути к постам '''
from django.urls import path
from posts.views import PostList, PostDetail

app_name='posts'
urlpatterns = [
    path('', PostList.as_view(), name='list'),
    path('<slug:slug>/', PostDetail.as_view(), name='detail'),
]
