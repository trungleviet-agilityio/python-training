# Django Security Best Practices

## Overview
This guide covers security best practices for Django projects, including authentication, authorization, data protection, and common security vulnerabilities.

## Authentication & Authorization

### 1. User Authentication
```python
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Custom password validation
from django.core.exceptions import ValidationError

def validate_password_strength(password):
    if len(password) < 12:
        raise ValidationError('Password must be at least 12 characters long')
    if not any(char.isdigit() for char in password):
        raise ValidationError('Password must contain at least one number')
    if not any(char.isupper() for char in password):
        raise ValidationError('Password must contain at least one uppercase letter')
```

### 2. Session Security
```python
# settings.py
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

### 3. Permission Management
```python
# views.py
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    fields = ['title', 'content']

# Custom permission decorator
from functools import wraps
from django.core.exceptions import PermissionDenied

def user_passes_test_with_message(test_func, message):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                raise PermissionDenied(message)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
```

## Data Protection

### 1. Sensitive Data Handling
```python
# models.py
from django.db import models
from django.conf import settings
from cryptography.fernet import Fernet

class SensitiveData(models.Model):
    encrypted_data = models.BinaryField()
    
    def set_data(self, data):
        f = Fernet(settings.ENCRYPTION_KEY)
        self.encrypted_data = f.encrypt(data.encode())
    
    def get_data(self):
        f = Fernet(settings.ENCRYPTION_KEY)
        return f.decrypt(self.encrypted_data).decode()
```

### 2. File Upload Security
```python
# forms.py
from django import forms
from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size
    if filesize > 5242880:  # 5MB
        raise ValidationError("Maximum file size is 5MB")

class DocumentForm(forms.Form):
    file = forms.FileField(
        validators=[validate_file_size],
        widget=forms.FileInput(attrs={'accept': '.pdf,.doc,.docx'})
    )
```

## Security Headers

### 1. Django Security Middleware
```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Security settings
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

## Common Vulnerabilities

### 1. CSRF Protection
```python
# views.py
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

@method_decorator(csrf_protect, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
```

### 2. XSS Prevention
```python
# templates/post_detail.html
{{ post.title|escape }}
{{ post.content|safe|escape }}
```

### 3. SQL Injection Prevention
```python
# Good - Using ORM
posts = Post.objects.filter(title__icontains=search_term)

# Bad - Raw SQL (avoid)
posts = Post.objects.raw(f"SELECT * FROM blog_post WHERE title LIKE '%{search_term}%'")
```

## API Security

### 1. JWT Authentication
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

# views.py
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
```

### 2. Rate Limiting
```python
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}
```

## Security Checklist

1. **Authentication**
   - [ ] Strong password policies
   - [ ] Multi-factor authentication
   - [ ] Session management
   - [ ] Password reset security

2. **Authorization**
   - [ ] Role-based access control
   - [ ] Permission checks
   - [ ] API authentication
   - [ ] Token management

3. **Data Protection**
   - [ ] Encryption at rest
   - [ ] Secure file uploads
   - [ ] Data backup security
   - [ ] PII handling

4. **Infrastructure**
   - [ ] HTTPS enforcement
   - [ ] Security headers
   - [ ] CORS configuration
   - [ ] Firewall rules

## Resources
- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Django Security Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) 