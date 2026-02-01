# LibraryProject - Advanced Features and Security

This Django project demonstrates advanced features including custom user models, permissions, groups, and security best practices.

## Project Structure

```
LibraryProject/
├── LibraryProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── bookshelf/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── bookshelf/
│           ├── book_list.html
│           └── form_example.html
└── manage.py
```

## Features

### 1. Custom User Model (Task 0)

The project uses a custom user model (`CustomUser`) that extends Django's `AbstractUser` with additional fields:

- **date_of_birth**: A DateField for storing user's birth date
- **profile_photo**: An ImageField for user profile pictures

#### Custom User Manager

The `CustomUserManager` handles user creation with the additional fields:

- `create_user()`: Creates regular users with email validation
- `create_superuser()`: Creates superusers with proper permission flags

#### Configuration

In `settings.py`:
```python
AUTH_USER_MODEL = 'bookshelf.CustomUser'
```

### 2. Permissions and Groups (Task 1)

#### Custom Permissions

The `Book` model includes custom permissions:

- `can_view`: Permission to view books
- `can_create`: Permission to create new books
- `can_edit`: Permission to edit existing books
- `can_delete`: Permission to delete books

#### Groups Setup

Create the following groups in Django Admin:

1. **Viewers**: Assign `can_view` permission
2. **Editors**: Assign `can_view`, `can_create`, and `can_edit` permissions
3. **Admins**: Assign all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`)

#### Permission Enforcement in Views

Views use the `@permission_required` decorator:

```python
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    ...

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    ...

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    ...

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    ...
```

### 3. Security Best Practices (Task 2)

#### Settings Configuration

```python
# Production settings
DEBUG = False

# Browser security headers
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True

# Cookie security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
```

#### CSRF Protection

All forms include the `{% csrf_token %}` template tag:

```html
<form method="post">
    {% csrf_token %}
    {{ form }}
    <button type="submit">Submit</button>
</form>
```

#### SQL Injection Prevention

Views use Django ORM with parameterized queries:

```python
# SECURE: Using Django ORM
books = Book.objects.filter(title__icontains=query)

# INSECURE (DO NOT USE):
# books = Book.objects.raw(f"SELECT * FROM bookshelf_book WHERE title LIKE '%{query}%'")
```

### 4. HTTPS and Secure Redirects (Task 3)

#### HTTPS Configuration

```python
# Redirect all HTTP to HTTPS
SECURE_SSL_REDIRECT = True

# HSTS settings
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

#### Deployment Notes

For production deployment:

1. Obtain SSL/TLS certificates (e.g., Let's Encrypt)
2. Configure your web server (Nginx/Apache) with SSL
3. Ensure `ALLOWED_HOSTS` is properly configured
4. Set a secure `SECRET_KEY`

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install django pillow
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Testing Permissions

1. Create test users in Django Admin
2. Create groups (Viewers, Editors, Admins) and assign permissions
3. Assign users to groups
4. Log in as different users and verify permission enforcement

## Security Checklist

- [x] Custom user model with additional fields
- [x] Custom permissions on Book model
- [x] Permission-protected views
- [x] CSRF protection on all forms
- [x] SQL injection prevention using ORM
- [x] XSS protection headers
- [x] Clickjacking protection (X-Frame-Options)
- [x] HTTPS redirect configuration
- [x] HSTS configuration
- [x] Secure cookie settings
