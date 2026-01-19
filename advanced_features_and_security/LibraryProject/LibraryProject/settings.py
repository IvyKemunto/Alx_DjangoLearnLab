"""
Django settings for LibraryProject project.

This settings file includes security best practices for production deployment.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5&x^m^=kjj)4j1u4xkmhp(*q18me%eww9t&mup3*c!d65+#(p6'

# =============================================================================
# SECURITY SETTINGS
# =============================================================================

# Set DEBUG to False in production to prevent sensitive information leakage
# DEBUG = False should be set in production environments
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# =============================================================================
# HTTPS AND SECURE REDIRECT SETTINGS (Task 3)
# =============================================================================

# Redirect all non-HTTPS requests to HTTPS
# This ensures all traffic is encrypted
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) settings
# Instructs browsers to only access the site via HTTPS for the specified time
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds

# Include all subdomains in the HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow the site to be included in browser HSTS preload lists
SECURE_HSTS_PRELOAD = True

# =============================================================================
# COOKIE SECURITY SETTINGS (Task 2 & 3)
# =============================================================================

# Ensure session cookies are only sent over HTTPS connections
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS connections
CSRF_COOKIE_SECURE = True

# =============================================================================
# BROWSER SECURITY HEADERS (Task 2 & 3)
# =============================================================================

# Enable the browser's XSS filtering to help prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True

# Prevent the site from being displayed in iframes to protect against clickjacking
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# =============================================================================
# CONTENT SECURITY POLICY (CSP) - Task 2
# =============================================================================
# Note: For full CSP implementation, consider using django-csp middleware
# The following headers provide baseline protection
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =============================================================================
# CUSTOM USER MODEL CONFIGURATION (Task 0)
# =============================================================================
# Point to the custom user model for all user-related functionality
AUTH_USER_MODEL = 'bookshelf.CustomUser'


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Media files configuration for profile photos
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
