from django.urls import path, include
from comments.views import CommentCreate


app_name='comments'
urlpatterns = [
    path('create_comment/', CommentCreate.as_view(), name='create_comment'),
]