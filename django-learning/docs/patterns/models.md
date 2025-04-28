# Model Patterns

This document covers common patterns used with Django models, focusing on organizing data and business logic effectively.

## Active Record Pattern

The Active Record pattern is Django's default model pattern. It maps database tables to Python classes and rows to objects.

### Basic Implementation

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
```

### Use Cases

- Simple CRUD operations
- Data representation
- Basic data validation

### Best Practices

- Keep models focused on data structure
- Use appropriate field types
- Implement `__str__` method
- Define Meta options when needed

## Model Mixins

Model mixins provide reusable functionality for models through inheritance.

### TimeStampedModel Mixin

```python
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Article(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

### SoftDeleteModel Mixin

```python
class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True
    
    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
```

### Use Cases

- Shared functionality across models
- Common fields or methods
- Reusable business logic

### Best Practices

- Keep mixins focused and single-purpose
- Use abstract models for mixins
- Document mixin behavior
- Consider model inheritance order

## Service Objects

Service objects encapsulate business logic that doesn't belong in models or views.

### Basic Service

```python
class ArticleService:
    @staticmethod
    def create_article(title, content, author):
        article = Article.objects.create(
            title=title,
            content=content,
            author=author
        )
        return article
    
    @staticmethod
    def publish_article(article_id):
        article = Article.objects.get(id=article_id)
        article.status = 'published'
        article.published_at = timezone.now()
        article.save()
        return article
```

### Complex Service

```python
class ArticlePublicationService:
    def __init__(self, article):
        self.article = article
    
    def publish(self):
        if not self.article.is_ready_for_publication():
            raise ValidationError("Article is not ready for publication")
        
        self.article.status = 'published'
        self.article.published_at = timezone.now()
        self.article.save()
        
        self._notify_author()
        self._create_social_media_posts()
        
        return self.article
    
    def _notify_author(self):
        # Send email notification
        pass
    
    def _create_social_media_posts(self):
        # Create social media posts
        pass
```

### Use Cases

- Complex business logic
- Operations involving multiple models
- External service integration
- Transaction management

### Best Practices

- Keep services focused on business logic
- Use static methods for simple operations
- Use instance methods for complex operations
- Handle exceptions appropriately
- Document service behavior

## Repository Pattern

The repository pattern abstracts data persistence operations.

### Basic Repository

```python
class ArticleRepository:
    @staticmethod
    def get_by_id(article_id):
        return Article.objects.get(id=article_id)
    
    @staticmethod
    def get_all():
        return Article.objects.all()
    
    @staticmethod
    def get_published():
        return Article.objects.filter(status='published')
```

### Advanced Repository

```python
class ArticleRepository:
    def __init__(self, model=Article):
        self.model = model
    
    def get_by_id(self, article_id):
        return self.model.objects.get(id=article_id)
    
    def get_all(self, filters=None, order_by=None):
        queryset = self.model.objects.all()
        
        if filters:
            queryset = queryset.filter(**filters)
        
        if order_by:
            queryset = queryset.order_by(order_by)
        
        return queryset
    
    def create(self, data):
        return self.model.objects.create(**data)
    
    def update(self, article_id, data):
        article = self.get_by_id(article_id)
        for key, value in data.items():
            setattr(article, key, value)
        article.save()
        return article
    
    def delete(self, article_id):
        article = self.get_by_id(article_id)
        article.delete()
```

### Use Cases

- Abstract data access
- Complex queries
- Caching strategies
- Testing data access

### Best Practices

- Keep repositories focused on data access
- Use appropriate methods for operations
- Handle exceptions properly
- Document repository behavior
- Consider caching strategies

## Model Managers

Model managers provide custom query methods for models.

### Basic Manager

```python
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='published')
    
    def by_author(self, author):
        return self.filter(author=author)
    
    def recent(self):
        return self.order_by('-created_at')[:5]

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, default='draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    objects = ArticleManager()
```

### Use Cases

- Custom query methods
- Reusable filters
- Complex queries
- Query optimization

### Best Practices

- Keep managers focused on queries
- Use descriptive method names
- Document manager methods
- Consider performance implications

## Model Signals

Signals allow decoupled applications to get notified when actions occur.

### Basic Signal

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Article)
def notify_author_on_publish(sender, instance, created, **kwargs):
    if not created and instance.status == 'published':
        # Send notification to author
        pass
```

### Use Cases

- Automated actions
- Cross-model updates
- External service integration
- Logging and auditing

### Best Practices

- Use signals sparingly
- Keep signal handlers simple
- Document signal behavior
- Consider performance implications
- Handle exceptions properly

## Resources

- [Django Models Documentation](https://docs.djangoproject.com/en/5.0/topics/db/models/)
- [Django Managers Documentation](https://docs.djangoproject.com/en/5.0/topics/db/managers/)
- [Django Signals Documentation](https://docs.djangoproject.com/en/5.0/topics/signals/) 