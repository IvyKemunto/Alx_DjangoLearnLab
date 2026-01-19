from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    """
    Form for creating and editing Book instances.
    Uses Django's ModelForm for automatic validation and sanitization.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'publication_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter publication year'}),
        }


class ExampleForm(forms.Form):
    """
    Example form demonstrating secure form handling.
    All inputs are automatically validated and sanitized by Django.
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your message', 'rows': 4})
    )
