from django.urls import path
from views import LibraryDetailView
from views import list_books


urlpatterns = [
    path("books", list_books, name='list_all_books')
    path("library/<int:id>", LibraryDetailView.as_view(), name='library')
]