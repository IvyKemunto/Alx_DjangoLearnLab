### 1. CREATE Operation
```python
from bookshelf.models import Book
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created: {book.title} by {book.author} ({book.publication_year})")
```
## Output:
Book created: 1984 by George Orwell (1949)
### 2. RETRIEVE Operation 
```python
retrieved_book = Book.objects.get(title="1984")
print(f"Retrieved: {retrieved_book.title} by {retrieved_book.author} ({retrieved_book.publication_year})")
all_books = Book.objects.all()
print(f"All books: {all_books}")
```
## Output:
Retrieved: 1984 by George Orwell (1949)
All books: <QuerySet [<Book: 1984>]>
### 3. UPDATE Operation
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(f"Updated title: {retrieved_book.title}")
```
## Output:
Updated title: Nineteen Eighty-Four
### 4. DELETE Operation
```python
retrieved_book.delete()
remaining_books = Book.objects.all()
print(f"Remaining books after deletion: {remaining_books}")
```
## Output:
(1, {'bookshelf.Book': 1})
Remaining books after deletion: <QuerySet []>
## Summary
All CRUD operations completed successfully!
Book model working correctly with Django ORM
