from rest_framework import serializers 

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'date_pub']
        read_only_fields = ['slug']
