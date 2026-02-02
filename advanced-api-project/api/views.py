from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from .models import Book
from .serializers import BookSerializer


class BookFilter(django_filters.FilterSet):
    """
    Custom filter for Book model allowing filtering by title, author, and publication_year.
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class BookListView(generics.ListAPIView):
    """
    ListView: Retrieves all books from the database.

    Features:
        - Filtering: Filter by title, author, and publication_year
        - Searching: Search by title and author name
        - Ordering: Order by title and publication_year

    Permissions:
        - Read-only access for unauthenticated users
        - Full access for authenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = BookFilter
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
