from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    ListView: Retrieves all books from the database.

    Features:
        - Filtering: Filter by title, author, and publication_year using DjangoFilterBackend
        - Searching: Search by title and author name using SearchFilter
        - Ordering: Order by title and publication_year using OrderingFilter

    Permissions:
        - Read-only access for unauthenticated users
        - Full access for authenticated users

    Query Parameters:
        - ?title=<value> - Filter by title
        - ?author=<value> - Filter by author name
        - ?publication_year=<value> - Filter by publication year
        - ?search=<value> - Search in title and author fields
        - ?ordering=<field> - Order by title or publication_year (use -field for descending)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


class BookDetailView(generics.RetrieveAPIView):
    """
    DetailView: Retrieves a single book by its ID.

    Permissions:
        - Read-only access for unauthenticated users
        - Full access for authenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    CreateView: Adds a new book to the database.

    Features:
        - Handles form submissions and data validation
        - Custom validation ensures publication_year is not in the future

    Permissions:
        - Only authenticated users can create books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    UpdateView: Modifies an existing book.

    Features:
        - Handles form submissions and data validation
        - Custom validation ensures publication_year is not in the future

    Permissions:
        - Only authenticated users can update books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DeleteView: Removes a book from the database.

    Permissions:
        - Only authenticated users can delete books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
