from rest_framework import serializers 

from posts.models import Post
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = ['content']

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'date_pub']
        read_only_fields = ['slug']
