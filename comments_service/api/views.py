from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.mixins import ListModelMixin
from posts.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import mixins



# class PostCreateAPIView(ListModelMixin, 
#                         CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    lookup_field = 'slug'
    serializer_class = PostSerializer


    def list(self, request):
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    
    def retrieve(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
