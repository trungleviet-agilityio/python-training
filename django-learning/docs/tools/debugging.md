# Django Debugging Guide for Beginners

## Overview
This guide covers debugging techniques and tools for Django projects, focusing on the fundamentals that every Django developer should know. It includes VS Code configuration, Django Debug Toolbar, and debugging tests.

## VS Code Configuration

### 1. Launch Configuration
```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Django: Run Server",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "runserver"
            ],
            "django": true,
            "justMyCode": true
        },
        {
            "name": "Django: Debug Tests",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "test",
                "--noinput"
            ],
            "django": true,
            "justMyCode": false
        },
        {
            "name": "Django: Debug Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "django": true,
            "justMyCode": true
        },
        {
            "name": "Django: Shell",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/manage.py",
            "args": [
                "shell"
            ],
            "django": true,
            "justMyCode": true
        }
    ]
}
```

### 2. Settings Configuration
```json
// .vscode/settings.json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.pylintArgs": [
        "--load-plugins=pylint_django",
        "--django-settings-module=config.settings"
    ],
    "python.analysis.extraPaths": [
        "${workspaceFolder}"
    ],
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticMode": "workspace",
    "python.analysis.autoImportCompletions": true,
    "python.analysis.indexing": true,
    "python.analysis.packageIndexDepths": [
        {
            "name": "django",
            "depth": 5
        }
    ]
}
```

## Django Debug Toolbar

### 1. Installation
```bash
pip install django-debug-toolbar
```

### 2. Configuration
```python
# settings.py
INSTALLED_APPS = [
    # ...
    'debug_toolbar',
]

MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

# Debug Toolbar settings
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
```

### 3. URL Configuration
```python
# urls.py
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    # ...
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
```

## Debugging Techniques

### 1. Using Breakpoints
```python
# views.py
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Set a breakpoint here
    breakpoint()  # Python's built-in debugger
    
    # Or use this for more control
    import pdb; pdb.set_trace()
    
    return render(request, 'blog/post_detail.html', {'post': post})
```

### 2. Debugging with pdb
```python
# Common pdb commands
# n (next) - Execute the next line
# s (step) - Step into a function call
# c (continue) - Continue execution until the next breakpoint
# p variable_name - Print a variable's value
# l (list) - Show the current location in the code
# q (quit) - Quit the debugger
# h (help) - Show help
```

### 3. Using ipdb (Enhanced pdb)
```bash
pip install ipdb
```

```python
# views.py
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Use ipdb for a better debugging experience
    import ipdb; ipdb.set_trace()
    
    return render(request, 'blog/post_detail.html', {'post': post})
```

## Debugging Tests

### 1. Debugging with VS Code
```python
# tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Post

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = Post.objects.create(
            title="Test Post",
            content="Test Content"
        )
    
    def test_post_detail_view(self):
        # Set a breakpoint here
        response = self.client.get(reverse('post-detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
```

### 2. Using pytest with --pdb
```bash
# Run tests with pdb on failures
pytest --pdb

# Run a specific test with pdb
pytest tests/test_views.py::PostViewTest::test_post_detail_view --pdb
```

### 3. Debugging with Django Test Client
```python
# tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse

class PostViewTest(TestCase):
    def test_post_create_view(self):
        client = Client()
        
        # Debug the request and response
        response = client.post(
            reverse('post-create'),
            {'title': 'New Post', 'content': 'New Content'}
        )
        
        # Print response details for debugging
        print(f"Status code: {response.status_code}")
        print(f"Content: {response.content}")
        
        self.assertEqual(response.status_code, 302)  # Redirect after success
```

## Logging for Debugging

### 1. Configure Logging
```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True,
        },
        'blog': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### 2. Using Logging in Code
```python
# views.py
import logging

logger = logging.getLogger(__name__)

def post_detail(request, pk):
    logger.debug(f"Accessing post detail for pk={pk}")
    
    try:
        post = Post.objects.get(pk=pk)
        logger.info(f"Found post: {post.title}")
    except Post.DoesNotExist:
        logger.error(f"Post with pk={pk} not found")
        raise Http404("Post not found")
    
    return render(request, 'blog/post_detail.html', {'post': post})
```

## Debugging Common Issues

### 1. Database Queries
```python
# Enable SQL query logging
from django.db import connection
from django.db import reset_queries
import time
import functools

def query_debugger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        reset_queries()
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {len(connection.queries)}")
        print(f"Finished in : {(end - start):.2f}s")
        return result
    return wrapper

# Use the decorator
@query_debugger
def get_posts():
    return Post.objects.all()
```

### 2. Template Rendering
```python
# Debug template rendering
from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist

def render_template_with_debug(template_name, context):
    try:
        return render_to_string(template_name, context)
    except TemplateDoesNotExist as e:
        print(f"Template not found: {e}")
        # List available templates
        from django.template.loader import get_template
        print("Available templates:")
        for template in get_template('').engine.template_loaders:
            print(f"- {template}")
        raise
```

### 3. Form Validation
```python
# Debug form validation
def process_form(request):
    form = PostForm(request.POST)
    if not form.is_valid():
        print("Form errors:")
        for field, errors in form.errors.items():
            print(f"{field}: {errors}")
        return render(request, 'form.html', {'form': form})
    
    form.save()
    return redirect('success')
```

## Best Practices

1. **Use Appropriate Debugging Tools**
   - VS Code debugger for step-by-step debugging
   - Django Debug Toolbar for request/response inspection
   - Logging for production debugging

2. **Debugging Strategy**
   - Start with logging to understand the flow
   - Use breakpoints for detailed inspection
   - Debug tests to ensure functionality

3. **Performance Considerations**
   - Disable debugging tools in production
   - Use selective debugging (specific modules or functions)
   - Profile code to identify bottlenecks

4. **Security**
   - Never expose debugging tools in production
   - Remove or disable debug settings before deployment
   - Use environment variables to control debugging

## Resources
- [VS Code Python Debugging](https://code.visualstudio.com/docs/python/debugging)
- [Django Debug Toolbar Documentation](https://django-debug-toolbar.readthedocs.io/)
- [Python Debugging with pdb](https://docs.python.org/3/library/pdb.html)
- [Django Logging Documentation](https://docs.djangoproject.com/en/stable/topics/logging/) 