# Update Operation

## Command to Update a Book Instance

```python
# Import the Book model
from bookshelf.models import Book

# First, retrieve the book to update
book = Book.objects.get(title="1984")

# Update the title from "1984" to "Nineteen Eighty-Four"
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Alternative method using update()
Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")
```

## Expected Output

```python
# Before update
print("Before update:")
print(f"Title: {book.title}")
# Output: Title: 1984

# After update
book.title = "Nineteen Eighty-Four"
book.save()

print("After update:")
print(f"Title: {book.title}")
# Output: Title: Nineteen Eighty-Four

# Display all attributes to confirm the update
print(f"Book ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

# Output:
# Book ID: 1
# Title: Nineteen Eighty-Four
# Author: George Orwell
# Publication Year: 1949

# Using the __str__ method
print(book)
# Output: Nineteen Eighty-Four by George Orwell (1949)
```

## Verification of Update

```python
# Verify the update by retrieving the book again
updated_book = Book.objects.get(id=book.id)
print(f"Updated title: {updated_book.title}")
# Output: Updated title: Nineteen Eighty-Four
```

**Note**: The book title has been successfully updated from "1984" to "Nineteen Eighty-Four" and saved to the database.
