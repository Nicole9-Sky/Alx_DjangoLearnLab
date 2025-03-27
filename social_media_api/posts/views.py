from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, permissions
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

class UserFeedView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        followed_users = request.user.following.all()  # Get users the current user follows
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Filter posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

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
    
    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
