from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.db.models import Q
from .forms import ExampleForm

# Create your views here.

The enforce the permissions 👇🏼
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Securely fetching a book using ORM
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_detail.html', {"book": book})

class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = "bookshelf/book_list.html"
    context_object_name = "books"
    permission_required = "bookshelf.can_view"

# Secure search functionality
def book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(Q(title_icontains=query) | Q(author_icontains=query))
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})