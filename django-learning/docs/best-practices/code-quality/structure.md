# Django Project Structure

This document outlines best practices for organizing a Django project structure to ensure maintainability, scalability, and readability.

## Basic Project Structure

```
project_root/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
├── src/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── tests/
│   │       ├── __init__.py
│   │       ├── test_models.py
│   │       ├── test_views.py
│   │       └── test_forms.py
│   └── users/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── urls.py
│       ├── views.py
│       └── tests/
│           ├── __init__.py
│           ├── test_models.py
│           ├── test_views.py
│           └── test_forms.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── core/
│   └── users/
├── media/
├── docs/
└── scripts/
```

## Directory Structure Explanation

### Root Directory

- `manage.py`: Django's command-line utility for administrative tasks
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation
- `.gitignore`: Git ignore file
- `.env`: Environment variables (not tracked in git)

### Source Directory (`src/`)

- `settings/`: Split settings for different environments
  - `base.py`: Base settings shared across environments
  - `development.py`: Development-specific settings
  - `production.py`: Production-specific settings
- `urls.py`: Project URL configuration
- `wsgi.py`: WSGI application for production
- `asgi.py`: ASGI application for async support

### Apps Directory (`apps/`)

Each app follows the same structure:
- `admin.py`: Admin interface configuration
- `apps.py`: App configuration
- `models.py`: Database models
- `urls.py`: URL patterns for the app
- `views.py`: View functions/classes
- `tests/`: Test files organized by type

### Static Files (`static/`)

- `css/`: CSS files
- `js/`: JavaScript files
- `images/`: Image files

### Templates (`templates/`)

- `base.html`: Base template
- App-specific template directories

### Media Files (`media/`)

- User-uploaded files
- Organized by content type

### Documentation (`docs/`)

- Project documentation
- API documentation
- Development guides

### Scripts (`scripts/`)

- Deployment scripts
- Database scripts
- Utility scripts

## Best Practices

### 1. App Organization

- Keep apps small and focused
- Follow the single responsibility principle
- Use meaningful app names
- Create a `core` app for shared functionality

### 2. Settings Organization

- Split settings by environment
- Use environment variables for sensitive data
- Keep base settings DRY
- Document all settings

### 3. URL Configuration

- Use URL namespacing
- Keep URLs organized by app
- Use meaningful URL names
- Document URL patterns

### 4. Static Files

- Use static file versioning
- Organize by file type
- Use meaningful file names
- Implement caching strategy

### 5. Templates

- Use template inheritance
- Keep templates organized by app
- Use meaningful template names
- Document template blocks

### 6. Testing

- Organize tests by type
- Use meaningful test names
- Follow testing best practices
- Maintain high test coverage

### 7. Documentation

- Keep documentation up-to-date
- Document all major components
- Include setup instructions
- Document deployment process

## Implementation Guidelines

### 1. Creating a New App

```bash
# Create the app in the apps directory
python manage.py startapp new_app apps/new_app

# Update INSTALLED_APPS in settings
INSTALLED_APPS = [
    ...
    'apps.new_app',
]
```

### 2. Organizing Models

```python
# apps/new_app/models.py
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class YourModel(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
```

### 3. Organizing Views

```python
# apps/new_app/views.py
from django.views.generic import ListView, DetailView
from .models import YourModel

class YourModelListView(ListView):
    model = YourModel
    template_name = 'new_app/list.html'
    context_object_name = 'objects'

class YourModelDetailView(DetailView):
    model = YourModel
    template_name = 'new_app/detail.html'
    context_object_name = 'object'
```

### 4. Organizing URLs

```python
# apps/new_app/urls.py
from django.urls import path
from . import views

app_name = 'new_app'

urlpatterns = [
    path('', views.YourModelListView.as_view(), name='list'),
    path('<int:pk>/', views.YourModelDetailView.as_view(), name='detail'),
]
```

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/misc/design-philosophies/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
