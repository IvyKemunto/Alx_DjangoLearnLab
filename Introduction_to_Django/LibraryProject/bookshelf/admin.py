from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.
    
    Customizes the admin interface to display and manage books effectively.
    """
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for better navigation
    list_filter = ('publication_year', 'author')
    
    # Enable search functionality
    search_fields = ('title', 'author')
    
    # Fields to display when editing a book
    fields = ('title', 'author', 'publication_year')
    
    # Ordering in the admin list
    ordering = ('title',)
