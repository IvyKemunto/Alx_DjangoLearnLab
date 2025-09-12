# Update Operation
## Command:
```python
# Get the book and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated title: {book.title}")
```
## Expected Output:
Updated title: Nineteen Eighty-Four
## Description:
This command updates the title of the existing book from "1984" to "Nineteen Eighty-Four" and saves the changes using the save() method.
