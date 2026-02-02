from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer handles serialization and deserialization of Book instances.

    Features:
        - Serializes all fields of the Book model
        - Custom validation to ensure publication_year is not in the future

    Validation:
        The validate_publication_year method checks that the publication year
        does not exceed the current year, preventing invalid future dates.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure publication_year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer handles serialization of Author instances with nested books.

    Features:
        - Serializes the author's name field
        - Includes a nested BookSerializer to serialize all related books
        - The 'books' field dynamically retrieves all books associated with the author

    Relationship Handling:
        The nested BookSerializer uses many=True and read_only=True to handle
        the one-to-many relationship between Author and Book.
        When an Author is serialized, all their associated books are included
        in the response as a nested array.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
