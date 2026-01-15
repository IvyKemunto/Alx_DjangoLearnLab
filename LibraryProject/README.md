# LibraryProject

A Django web application for managing a library system.

## Getting Started

### Prerequisites
- Python 3.x
- Django 6.0.1

### Installation

1. Clone the repository
2. Install Django:
   ```bash
   pip install Django
   ```

### Running the Application

1. Navigate to the project directory:
   ```bash
   cd LibraryProject
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the development server:
   ```bash
   python manage.py runserver
   ```

4. Visit `http://127.0.0.1:8000/` in your web browser

## Project Structure

- **LibraryProject/**: Main project directory containing settings and configuration
  - `settings.py`: Django project configuration
  - `urls.py`: URL routing configuration
  - `wsgi.py`: WSGI configuration for deployment
- **manage.py**: Django command-line utility
- **bookshelf/**: Django app for managing books
  - `models.py`: Database models
  - `views.py`: View functions
  - `admin.py`: Admin interface configuration

## Apps

### bookshelf
Handles book management functionality including:
- Book model with title, author, and publication year
- Admin interface integration
- CRUD operations via Django shell

## Development

To create a superuser for admin access:
```bash
python manage.py createsuperuser
```

Access the admin interface at `http://127.0.0.1:8000/admin/`
