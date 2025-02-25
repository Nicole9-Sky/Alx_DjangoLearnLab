from django.shortcuts import render 
from relationship_app.models import Book, Library 
from django.view.generic import ListView


# Create your views here
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", context={'books': books})


class ListBookView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'