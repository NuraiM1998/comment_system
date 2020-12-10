from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.mixins import ListModelMixin
from posts.models import Post
from comments.models import Comment
from .serializers import (
    PostSerializer, 
    CommentSerializer, 
    FavoritePostSerializer, 
    AddPostFavoriteSerializer,
    DeletePostFavoriteSerializer
)    
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .mixins import ActionFavoriteMixin


class PostViewSet(ActionFavoriteMixin, viewsets.ModelViewSet):

    queryset = Post.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_serializer_class(self):
        if self.action == 'favorite':
            return FavoritePostSerializer
        elif self.action == 'add_to_favorite':
            return AddPostFavoriteSerializer
        elif self.action == 'delete_from_favorite':
            return DeletePostFavoriteSerializer
        return PostSerializer


    def favorite(self, request):
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)
    

    def add_to_favorite(self, request):
        super().action_with_favorite(request) 
        return Response(request.data)                                                                                                                                                                                                                                                                                                                                                                                                                                

    
    def delete_from_favorite(self, request):
        super().action_with_favorite(request)
        return Response(request.data)      


class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get_queryset(self):
        return self.queryset.filter(post__slug=self.kwargs.get('slug'))


    def perform_create(self, serializer):
        post = Post.objects.get(slug=self.kwargs.get("slug"))
        serializer.save(user=self.request.user, post=post)
