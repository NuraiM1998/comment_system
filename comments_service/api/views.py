from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.mixins import ListModelMixin
from posts.models import Post
from comments.models import Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import mixins


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer


    # def list(self, request):
    #     serializer = PostSerializer(self.queryset, many=True)
    #     return Response(serializer.data)
    
    
    # def retrieve(self, request, slug):
    #     post = get_object_or_404(Post, slug=slug)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data)

    
    # def destroy(self, request, *args, **kwargs):
    #     try:
    #         post = self.get_object()
    #         self.perform_destroy(post)
    #     except Http404:
    #         pass
    #     return Response(status=status.HTTP_204_NO_CONTENT)

        # instance = self.get_object()
        # self.perform_destroy(instance)
        # return Response(status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.select_related('post')
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_slug = self.kwargs.get("slug")
        try:
            post = Post.objects.get(slug=post_slug)
        except Post.DoesNotExist:
            pass
        return self.queryset.filter(post=post)
