# relationship_app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic import DetailView, ListView
from .models import Library

# Function-based view for listing books
def list_books(request):
    books = Book.objects.all()
    return HttpResponse(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template
    context_object_name = "library"
