from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for CustomUser model.
    Extends UserAdmin to include additional fields: date_of_birth and profile_photo.
    """
    model = CustomUser

    # Fields to display in the admin list view
    list_display = ('username', 'email', 'date_of_birth', 'is_staff', 'is_active')

    # Fields to filter by in the admin sidebar
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'groups')

    # Fields to search by
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Ordering of records
    ordering = ('username',)

    # Fieldsets for the user edit form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fieldsets for the user creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active'),
        }),
    )


class BookAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for Book model.
    """
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')


# Register models with admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)
