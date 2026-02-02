"""
Unit Tests for Book API Endpoints

This module contains comprehensive unit tests for testing the Book API endpoints
including CRUD operations, filtering, searching, ordering, and permission checks.

Testing Strategy:
- Test all CRUD operations (Create, Read, Update, Delete)
- Test authentication and permission enforcement
- Test filtering, searching, and ordering functionality
- Verify correct status codes and response data

To run tests: python manage.py test api
"""

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test cases for Book API endpoints.
    """

    def setUp(self):
        """
        Set up test data and authentication.
        """
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create test author
        self.author = Author.objects.create(name='Test Author')

        # Create test book
        self.book = Book.objects.create(
            title='Test Book',
            publication_year=2023,
            author=self.author
        )

        # Set up API client
        self.client = APIClient()

    def test_list_books_unauthenticated(self):
        """
        Test that unauthenticated users can list books (read-only access).
        """
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book_unauthenticated(self):
        """
        Test that unauthenticated users can retrieve a single book.
        """
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_create_book_unauthenticated(self):
        """
        Test that unauthenticated users cannot create books.
        """
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.pk
        }
        response = self.client.post(url, data)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_create_book_authenticated(self):
        """
        Test that authenticated users can create books.
        """
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book_authenticated(self):
        """
        Test that authenticated users can update books.
        """
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_update_book_unauthenticated(self):
        """
        Test that unauthenticated users cannot update books.
        """
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.put(url, data)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_delete_book_authenticated(self):
        """
        Test that authenticated users can delete books.
        """
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        """
        Test that unauthenticated users cannot delete books.
        """
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_filter_books_by_title(self):
        """
        Test filtering books by title.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'title': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_author(self):
        """
        Test filtering books by author name.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'Test Author'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_books_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'publication_year': 2023})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """
        Test searching books by title.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_by_title(self):
        """
        Test ordering books by title.
        """
        # Create another book for ordering test
        Book.objects.create(
            title='Another Book',
            publication_year=2022,
            author=self.author
        )
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')

    def test_order_books_by_publication_year(self):
        """
        Test ordering books by publication year.
        """
        Book.objects.create(
            title='Older Book',
            publication_year=2020,
            author=self.author
        )
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)

    def test_publication_year_validation(self):
        """
        Test that publication year cannot be in the future.
        """
        self.client.login(username='testuser', password='testpass123')
        url = reverse('book-create')
        data = {
            'title': 'Future Book',
            'publication_year': 2030,
            'author': self.author.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
