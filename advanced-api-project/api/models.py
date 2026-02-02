from django.db import models


class Author(models.Model):
    """
    Author model represents a book author.

    Fields:
        name: A string field to store the author's name.

    Relationships:
        One-to-Many with Book model - An author can have multiple books.
        The related_name 'books' allows accessing all books by an author
        via author.books.all()
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model represents a book in the library.

    Fields:
        title: A string field for the book's title.
        publication_year: An integer field for the year the book was published.
        author: A foreign key linking to the Author model.

    Relationships:
        Many-to-One with Author model - Each book belongs to one author.
        The on_delete=CASCADE ensures that when an author is deleted,
        all their books are also deleted.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
