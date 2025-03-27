from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Show 5 posts per page
    page_size_query_param = 'page_size'
    max_page_size = 100
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination

def perform_create(self, serializer):
    serializer.save(author=self.request.user)
    
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
    def get_query_set(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
