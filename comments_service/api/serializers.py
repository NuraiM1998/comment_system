from rest_framework import serializers 

from posts.models import Post
from comments.models import Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class PostSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='post_api:post-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Post
        fields = ['url', 'title', 'slug', 'body', 'date_pub']
        read_only_fields = ['slug']


class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['id', 'content', 'post']
        read_only_fields = ['user', 'post']
