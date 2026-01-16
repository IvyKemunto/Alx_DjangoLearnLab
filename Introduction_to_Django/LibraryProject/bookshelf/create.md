# Create Operation
## Command:
```python
from bookshelf.models import Book
# Create a Book instance using Book.objects.create()
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Verify creation
print(f"Book created: {book.title} by {book.author} ({book.publication_year})")
```
## Expected Output:
Book created: 1984 by George Orwell (1949)
## Description:
This command creates a new Book instance with the specified title, author, and publication year using the Book.objects.create() method.
