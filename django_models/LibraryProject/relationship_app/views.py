from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from .models import Library

# Function-based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'