from django.shortcuts import render
from .models import Book  

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library  


class LibraryDetailView(DetailView):
    model = Library  # Specifies the model to use
    template_name = 'library_detail.html'  # Specifies the template
    context_object_name = 'library'