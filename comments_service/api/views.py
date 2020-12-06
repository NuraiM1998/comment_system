from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.mixins import ListModelMixin
from posts.models import Post
from comments.models import Comment
from .serializers import PostSerializer, CommentSerializer, FavoritePostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        print(self.action)
        if self.action == 'favorite':
            return FavoritePostSerializer
        return PostSerializer

    def favorite(self, request):
        print("favorite")
        print('>>>>>>', request.user)
        # serializer = self.get_serializer(instance=request.user)
        # print('>>>>>>', serializer.data)
        return Response({})
    

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return self.queryset.filter(post__slug=self.kwargs.get('slug'))


    def perform_create(self, serializer):
        post = Post.objects.get(slug=self.kwargs.get("slug"))
        serializer.save(user=self.request.user, post=post)
