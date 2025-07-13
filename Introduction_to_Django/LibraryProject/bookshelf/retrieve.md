
# Retrieve Operation
## Command:
```python
# Retrieve the book by title
retrieved_book = Book.objects.get(title="1984")
print(f"Retrieved: {retrieved_book.title} by {retrieved_book.author} ({retrieved_book.publication_year})")

# Show all books
all_books = Book.objects.all()
print(f"All books: {all_books}")
```
## Expected Output:
Retrieved: 1984 by George Orwell (1949)
All books: <QuerySet [<Book: 1984>]>
## Description:
This command retrieves the book with the title "1984" from the database using Book.objects.get() and displays all books using Book.objects.all().
