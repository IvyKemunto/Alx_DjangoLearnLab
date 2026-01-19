from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm, ExampleForm


# =============================================================================
# PERMISSION-PROTECTED VIEWS (Task 1)
# =============================================================================
# These views enforce permissions using the @permission_required decorator.
# Users must have the appropriate permission assigned (directly or via groups)
# to access these views.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to display a list of all books.
    Requires 'can_view' permission.
    Uses Django ORM to safely query the database (prevents SQL injection).
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    """
    View to create a new book.
    Requires 'can_create' permission.
    Uses Django forms for input validation and sanitization.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Using Django ORM's create method prevents SQL injection
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'title': 'Add New Book',
        'action': 'Create'
    })


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    """
    View to edit an existing book.
    Requires 'can_edit' permission.
    Uses get_object_or_404 for safe object retrieval.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'title': f'Edit Book: {book.title}',
        'action': 'Update'
    })


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    """
    View to delete a book.
    Requires 'can_delete' permission.
    Uses get_object_or_404 for safe object retrieval.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})


# =============================================================================
# SECURE FORM EXAMPLE (Task 2)
# =============================================================================

def form_example(request):
    """
    Example view demonstrating secure form handling.
    - Uses Django forms for input validation
    - Template includes CSRF token for protection
    - All user inputs are sanitized through form validation
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the validated and sanitized data
            # Django forms automatically escape and validate input
            pass
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {
        'form': form,
        'title': 'Example Form',
        'action': 'Submit'
    })


# =============================================================================
# SEARCH FUNCTIONALITY WITH SQL INJECTION PREVENTION (Task 2)
# =============================================================================

def search_books(request):
    """
    Secure search view demonstrating SQL injection prevention.
    Uses Django ORM's parameterized queries instead of raw SQL.
    """
    query = request.GET.get('q', '')

    # SECURE: Using Django ORM with parameterized queries
    # This prevents SQL injection attacks
    if query:
        # Using Django's ORM filter with __icontains is safe
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    # INSECURE EXAMPLE (DO NOT USE):
    # Never use string formatting with raw SQL:
    # books = Book.objects.raw(f"SELECT * FROM bookshelf_book WHERE title LIKE '%{query}%'")

    return render(request, 'bookshelf/book_list.html', {
        'books': books,
        'search_query': query
    })
