# Delete Operation

## Command to Delete a Book Instance

```python
# Import the Book model
from bookshelf.models import Book

# First, retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")  # or use get(id=1)

# Method 1: Delete the specific instance
book.delete()

# Alternative Method 2: Delete using filter and delete()
Book.objects.filter(title="Nineteen Eighty-Four").delete()

# Alternative Method 3: Delete by ID
Book.objects.filter(id=1).delete()
```

## Expected Output

```python
# Before deletion - verify the book exists
try:
    book = Book.objects.get(title="Nineteen Eighty-Four")
    print(f"Book found: {book}")
    print(f"Book ID: {book.id}")
except Book.DoesNotExist:
    print("Book not found")

# Output before deletion:
# Book found: Nineteen Eighty-Four by George Orwell (1949)
# Book ID: 1

# Delete the book
book.delete()
# Output: (1, {'bookshelf.Book': 1})
# This indicates 1 object was deleted

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Total books in database: {all_books.count()}")
print("All books:")
for book in all_books:
    print(f"- {book}")

# Output after deletion:
# Total books in database: 0
# All books:
# (no books listed)
```

## Verification of Deletion

```python
# Try to retrieve the deleted book
try:
    deleted_book = Book.objects.get(title="Nineteen Eighty-Four")
    print(f"Book still exists: {deleted_book}")
except Book.DoesNotExist:
    print("Book successfully deleted - not found in database")

# Output:
# Book successfully deleted - not found in database

# Double-check with all books
print(f"Books remaining: {Book.objects.all().count()}")
# Output: Books remaining: 0
```

**Note**: The book instance has been successfully deleted from the database. Attempting to retrieve it now raises a `DoesNotExist` exception, confirming the deletion was successful.
