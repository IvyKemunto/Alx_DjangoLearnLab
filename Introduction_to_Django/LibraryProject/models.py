from django.db import models

# Create your models here.

class Book(models.Model):
    """
    Book model representing a book in the library system.
    
    Attributes:
        title: CharField with maximum length of 200 characters
        author: CharField with maximum length of 100 characters  
        publication_year: IntegerField for the year the book was published
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        """String representation of the Book model"""
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        """Meta options for the Book model"""
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']
