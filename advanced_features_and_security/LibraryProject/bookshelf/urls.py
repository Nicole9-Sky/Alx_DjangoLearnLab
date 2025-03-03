from django.urls import path 
from . import views_books, create_book, edit_book, delete_book

urlpatterns[
    path('view_books/', views_books, name='view_books'),
    path('create_book/', create_book, name='create_book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
]