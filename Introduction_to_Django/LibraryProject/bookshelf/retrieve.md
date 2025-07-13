```python
retrieved_book = Book.objects.get(title="1984")
print(f"Retrieved: {retrieved_book.title} by {retrieved_book.author} ({retrieved_book.publication_year})")

print(f"All books: {all_books}")
```
## Expected Output:
Retrieved: 1984 by George Orwell (1949)
All books: <QuerySet [<Book: 1984>]>
## Description:
This command retrieves the book with the title "1984" from the database and displays all books.
