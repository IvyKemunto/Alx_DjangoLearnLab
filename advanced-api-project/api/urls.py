from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # List all books - GET /books/
    path('books/', BookListView.as_view(), name='book-list'),

    # Retrieve a single book by ID - GET /books/<id>/
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create a new book - POST /books/create/
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update a book - PUT /books/<id>/update/
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # Delete a book - DELETE /books/<id>/delete/
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
