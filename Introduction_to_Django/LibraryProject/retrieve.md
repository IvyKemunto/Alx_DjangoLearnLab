# Retrieve Operation

## Command to Retrieve a Book Instance

```python
# Import the Book model
from bookshelf.models import Book

# Retrieve the book by ID (assuming the book with ID=1 exists)
book = Book.objects.get(id=1)

# Alternative methods to retrieve books
# Get by title
book = Book.objects.get(title="1984")

# Get all books
all_books = Book.objects.all()

# Filter books by author
orwell_books = Book.objects.filter(author="George Orwell")
```

## Expected Output

```python
# Display all attributes of the retrieved book
print(f"Book ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

# Output:
# Book ID: 1
# Title: 1984
# Author: George Orwell
# Publication Year: 1949

# Using the __str__ method
print(book)
# Output: 1984 by George Orwell (1949)
```

## Additional Retrieval Examples

```python
# Check if book exists
try:
    book = Book.objects.get(title="1984")
    print(f"Found book: {book}")
except Book.DoesNotExist:
    print("Book not found")

# Get all books and display them
for book in Book.objects.all():
    print(f"- {book}")
```

**Note**: The book instance has been successfully retrieved from the database showing all its attributes.
