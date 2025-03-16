from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Book, Author

class BookAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Unknown Author")
        self.book1 = Book.objects.create(title="Django for Beginners", author=self.author, publication_year=2021)

    def test_create_book(self):
        self.client.login(username="testuser", password="testpassword")
        data = {
            "title": "New Django Book",
            "author": self.author.id,  # Fix: Use author ID
            "publication_year": 2022  # Fix: Use 'publication_year' instead of 'published_date'
        }
        response = self.client.post("/api/books/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Django Book")  # Check response data
