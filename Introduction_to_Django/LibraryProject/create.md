# Create Operation

## Command to Create a Book Instance

```python
# Import the Book model
from bookshelf.models import Book

# Create a Book instance
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Alternative method using create()
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output

```
# After creating and saving the book
Book object (1)  # The number may vary depending on database state

# When using the __str__ method
print(book)
# Output: 1984 by George Orwell (1949)
```

## Verification

```python
# Verify the book was created
print(f"Book ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

**Note**: The book instance has been successfully created and saved to the database with the specified attributes.
