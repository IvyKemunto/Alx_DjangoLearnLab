from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

"""
Authentication and Permissions Setup:

This API uses Token-based authentication provided by Django REST Framework.

To obtain a token:
- Send a POST request to /api-token-auth/ with username and password
- This uses DRF's built-in view: obtain_auth_token from rest_framework.authtoken.views

To use the token:
- Include the token in the Authorization header: "Authorization: Token <your_token>"

Permissions:
- BookList (GET /api/books/): No authentication required - public access
- BookViewSet (CRUD /api/books_all/): Requires authentication (IsAuthenticated)
"""


class BookList(generics.ListAPIView):
    """
    API view to retrieve list of all books.
    No authentication required for this view.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for handling all CRUD operations on Book model.

    Authentication: Token-based authentication is required.
    Users must obtain a token via /api-token-auth/ endpoint using
    DRF's built-in obtain_auth_token view.

    Permissions: Only authenticated users can access this viewset.
    Uses IsAuthenticated permission class.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
