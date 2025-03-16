from django.test import TestCase
from api.models import Book, Author  # Import the correct models

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create an author first
        self.author = Author.objects.create(name="Unknown Author")

        # Create a book using the author instance
        self.book1 = Book.objects.create(title="Django for Beginners", author=self.author, publication_year=2021)

    def test_create_book(self):
        self.assertEqual(self.book1.title, "Django for Beginners")
