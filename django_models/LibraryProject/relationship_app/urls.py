from .models import Book, Author, Library, Librarian

author_name = Author.objects.create(name="Limah")
author_name.save()

author = Author.objects.get(name=author_name)
author = Author.objects.filter(author = author)

author_name = author.objects.filter(author = author)
book = Book.objects.create(title="Python", author=author_name)
book.save()
book = Book.objects.create(title="Flask", author=author_name)
book.save()
library_name = Library.objects.create(name = "HardCopySections", book = book)
library_name.save()
librarian_name = Librarian(name = "Palmer")
librarian_name.save()

# Query all books by a specific author.
book = Book.objects.filter(author=1)
print(book.values())

# List all books in a library.
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library.
librarian = Librarian.objects.get(library=librarian_name)
print(librarian_name)

#  ["Librarian.objects.get(library="]
#  ["objects.filter(author=author)"]