```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
remaining_books = Book.objects.all()
print(f"Remaining books after deletion: {remaining_books}")
```
## Expected Output:
(1, {'bookshelf.Book': 1})
Remaining books after deletion: <QuerySet []>
## Description:
This command deletes the book instance from the database using the delete() method and confirms the deletion.
