from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user manager for CustomUser model.
    Handles user creation with additional fields like date_of_birth and profile_photo.
    """

    def create_user(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and return a regular user with the given username, email, password,
        and optional date_of_birth and profile_photo.
        """
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        """
        Create and return a superuser with the given username, email, password,
        and optional date_of_birth and profile_photo.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            username=username,
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo,
            **extra_fields
        )


class CustomUser(AbstractUser):
    """
    Custom User model extending AbstractUser with additional fields:
    - date_of_birth: User's date of birth
    - profile_photo: User's profile photo
    """
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Book(models.Model):
    """
    Book model with custom permissions for access control.
    Permissions:
    - can_view: Permission to view books
    - can_create: Permission to create new books
    - can_edit: Permission to edit existing books
    - can_delete: Permission to delete books
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title
