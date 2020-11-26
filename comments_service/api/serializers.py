from rest_framework import serializers 

from posts.models import Post
from comments.models import Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'date_pub']
        read_only_fields = ['slug']


class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer
    post = PostSerializer
    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'post']
        read_only_fields = ['user', 'post']
