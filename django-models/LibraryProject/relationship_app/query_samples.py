from .models import Book, Author, Library, Librarian

# Create an author
author = Author.objects.create(name="Limah")

# Create books and associate them with the author
book1 = Book.objects.create(title="Python", author=author)
book2 = Book.objects.create(title="Flask", author=author)

# Create a library and add books
library = Library.objects.create(name="HardCopySections")
library.books.add(book1, book2)

# Create a librarian and assign them to the library
librarian = Librarian.objects.create(name="Palmer", library=library)

# Query all books by a specific author
books_by_author = Book.objects.filter(author=author)
print(books_by_author.values())

# List all books in a library
books_in_library = library.books.all()
print(books_in_library.values())

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(librarian.name)
