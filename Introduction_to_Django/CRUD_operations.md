# CRUD Operations Documentation

This document demonstrates the Create, Retrieve, Update, and Delete operations for the Book model in the Django shell.

## Prerequisites

Before executing these commands, ensure you have:
1. Created the Django project and bookshelf app
2. Defined the Book model in `bookshelf/models.py`
3. Added 'bookshelf' to INSTALLED_APPS in settings.py
4. Run migrations: `python manage.py makemigrations bookshelf` and `python manage.py migrate`
5. Started Django shell: `python manage.py shell`

## 1. CREATE Operation

### Command:
```python
from bookshelf.models import Book

# Create a Book instance with the specified attributes
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Alternative method
# book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

### Expected Output:
```python
# After saving, the book object gets an ID
print(book.id)  # Output: 1 (or next available ID)
print(book)     # Output: 1984 by George Orwell (1949)
```

**Result**: A new Book instance has been successfully created and saved to the database.

---

## 2. RETRIEVE Operation

### Command:
```python
from bookshelf.models import Book

# Retrieve the book we just created
book = Book.objects.get(title="1984")

# Display all attributes
print(f"ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

### Expected Output:
```python
# Output:
ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949

# Using __str__ method
print(book)  # Output: 1984 by George Orwell (1949)
```

**Result**: The book instance has been successfully retrieved, displaying all its attributes.

---

## 3. UPDATE Operation

### Command:
```python
from bookshelf.models import Book

# Retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title from "1984" to "Nineteen Eighty-Four"
book.title = "Nineteen Eighty-Four"
book.save()
```

### Expected Output:
```python
# Before update
print("Original title: 1984")

# After update
print(f"Updated title: {book.title}")  # Output: Updated title: Nineteen Eighty-Four
print(book)  # Output: Nineteen Eighty-Four by George Orwell (1949)
```

**Result**: The book's title has been successfully updated from "1984" to "Nineteen Eighty-Four".

---

## 4. DELETE Operation

### Command:
```python
from bookshelf.models import Book

# Retrieve the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm deletion by trying to retrieve all books
all_books = Book.objects.all()
print(f"Number of books: {all_books.count()}")
```

### Expected Output:
```python
# Delete operation returns a tuple with count of deleted objects
# Output: (1, {'bookshelf.Book': 1})

# Confirmation of deletion
print(f"Number of books: {all_books.count()}")  # Output: Number of books: 0

# Trying to retrieve the deleted book
try:
    Book.objects.get(title="Nineteen Eighty-Four")
except Book.DoesNotExist:
    print("Book successfully deleted")  # This will be executed
```

**Result**: The book instance has been successfully deleted from the database.

---

## Summary

All CRUD operations have been successfully demonstrated:

1. **CREATE**: ✅ Created a Book instance with title "1984", author "George Orwell", publication year 1949
2. **RETRIEVE**: ✅ Retrieved the book and displayed all its attributes  
3. **UPDATE**: ✅ Updated the title from "1984" to "Nineteen Eighty-Four"
4. **DELETE**: ✅ Deleted the book instance and confirmed deletion

## Additional Notes

- All operations use Django's ORM (Object-Relational Mapping)
- The Book model includes proper `__str__` method for readable representations
- Error handling with `try/except` blocks is recommended for real applications
- The operations can be executed individually or as part of a larger script
