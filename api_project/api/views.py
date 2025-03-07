from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .permissions import IsAdminOrReadOnly

# Create your views here.

class BookList(ListAPIView):
    """
    ListAPIView for the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class BookViewSet(viewsets.ModelViewSet):
    
    """
    ViewSet for handling all CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


    