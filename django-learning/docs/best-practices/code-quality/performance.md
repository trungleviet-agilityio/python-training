# Django Performance Optimization Guide

## Overview
This guide covers performance optimization techniques for Django projects, including database optimization, caching, and code-level improvements.

## Database Optimization

### 1. Query Optimization
```python
# Bad - N+1 query problem
posts = Post.objects.all()
for post in posts:
    print(post.author.username)  # Makes a query for each post

# Good - Using select_related
posts = Post.objects.select_related('author').all()
for post in posts:
    print(post.author.username)  # No additional queries

# Bad - Multiple queries for many-to-many
posts = Post.objects.all()
for post in posts:
    print(post.tags.all())  # Makes a query for each post

# Good - Using prefetch_related
posts = Post.objects.prefetch_related('tags').all()
for post in posts:
    print(post.tags.all())  # No additional queries
```

### 2. Bulk Operations
```python
# Bad - Multiple queries
for title in titles:
    Post.objects.create(title=title)

# Good - Bulk create
Post.objects.bulk_create([
    Post(title=title) for title in titles
])

# Bad - Multiple updates
for post in Post.objects.all():
    post.status = 'published'
    post.save()

# Good - Bulk update
Post.objects.all().update(status='published')
```

### 3. Database Indexing
```python
# models.py
class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['author', 'status']),
        ]
```

## Caching

### 1. View Caching
```python
# views.py
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

@method_decorator(cache_page(60 * 15), name='dispatch')
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
```

### 2. Template Fragment Caching
```python
# templates/post_list.html
{% load cache %}

{% cache 500 sidebar %}
    <div class="sidebar">
        {% for category in categories %}
            <a href="{{ category.get_absolute_url }}">{{ category.name }}</a>
        {% endfor %}
    </div>
{% endcache %}
```

### 3. Query Caching
```python
# models.py
from django.core.cache import cache

class PostManager(models.Manager):
    def get_popular_posts(self):
        cache_key = 'popular_posts'
        posts = cache.get(cache_key)
        
        if posts is None:
            posts = self.filter(status='published').order_by('-views')[:5]
            cache.set(cache_key, posts, 60 * 15)  # Cache for 15 minutes
        
        return posts
```

## Code Optimization

### 1. Lazy Loading
```python
# Bad - Eager loading
posts = list(Post.objects.all())

# Good - Lazy loading
posts = Post.objects.all()
for post in posts:  # Query executed only when needed
    print(post.title)
```

### 2. Pagination
```python
# views.py
from django.core.paginator import Paginator

def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 25)  # Show 25 posts per page
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/post_list.html', {'posts': posts})
```

### 3. Async Views
```python
# views.py
from django.http import HttpResponse
import asyncio

async def async_view(request):
    await asyncio.sleep(1)  # Simulate async operation
    return HttpResponse("Hello, async world!")
```

## Static Files

### 1. Static Files Optimization
```python
# settings.py
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Collect static files
python manage.py collectstatic --noinput
```

### 2. Media Files
```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Use cloud storage for production
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
```

## Monitoring and Profiling

### 1. Django Debug Toolbar
```python
# settings.py
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = ['127.0.0.1']
```

### 2. Performance Monitoring
```python
# middleware.py
import time
from django.db import connection

class QueryCountDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        initial_queries = len(connection.queries)
        start_time = time.time()
        
        response = self.get_response(request)
        
        final_queries = len(connection.queries)
        execution_time = time.time() - start_time
        
        print(f"Number of queries: {final_queries - initial_queries}")
        print(f"Execution time: {execution_time:.2f} seconds")
        
        return response
```

## Best Practices

1. **Database**
   - Use appropriate indexes
   - Optimize queries
   - Use bulk operations
   - Monitor query performance

2. **Caching**
   - Cache expensive operations
   - Use appropriate cache backends
   - Set reasonable cache timeouts
   - Monitor cache hit rates

3. **Code**
   - Use lazy loading
   - Implement pagination
   - Optimize loops
   - Use async where appropriate

4. **Static Files**
   - Use CDN for static files
   - Enable compression
   - Optimize images
   - Use appropriate storage backends

## Resources
- [Django Performance Documentation](https://docs.djangoproject.com/en/stable/topics/performance/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)
- [Django Cache Framework](https://docs.djangoproject.com/en/stable/topics/cache/) 