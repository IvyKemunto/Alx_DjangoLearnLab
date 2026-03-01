from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Profile
from taggit.forms import TagWidget


class CustomUserCreationForm(UserCreationForm):
    """Extended user registration form with email field."""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    """Form for updating user profile."""
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class UserUpdateForm(forms.ModelForm):
    """Form for updating user information."""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    """Form for creating and updating blog posts."""
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Write your post content here...'}),
            'tags': TagWidget(attrs={'class': 'form-control', 'placeholder': 'Enter tags separated by commas'}),
        }


class CommentForm(forms.ModelForm):
    """Form for creating and updating comments."""
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your comment here...'}),
        }
