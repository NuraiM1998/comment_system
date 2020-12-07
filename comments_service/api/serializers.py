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


class FavoritePostSerializer(UserSerializer):

    posts = PostSerializer(source='favorite_set', many=True)
    # posts = serializers.SerializerMethodField(method_name='get_favorite_posts')

    # def get_favorite_posts(self, obj):
    #     serializer = PostSerializer(obj.favorite_set.all(), 
    #                                 context=self.context, 
    #                                 many=True
    #                             )
    #     return serializer.data

    class Meta(UserSerializer.Meta):
        fields = ['posts']


class AddPostFavoriteSerializer(serializers.Serializer):
    
    post_slug = serializers.CharField(min_length=1)

    def validate_post_slug(self, post_slug):
        if not Post.objects.filter(slug=post_slug).exists():
            raise serializers.ValidationError("Post doesn't exist")
        return post_slug

    def save(self):
        post_slug = self.validated_data['post_slug']
        post = Post.objects.get(slug=post_slug)
        request = self.context.get('request')
        user = request.user
        user.favorite_set.add(post)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'content', 'post']
        read_only_fields = ['user', 'post']
