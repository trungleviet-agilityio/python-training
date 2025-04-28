# Business Logic Patterns

This document covers common patterns used for organizing business logic in Django applications, focusing on maintainability, reusability, and testability.

## Service Layer Pattern

The service layer pattern separates business logic from views and models.

### Basic Service

```python
class ArticleService:
    def create_article(self, title, content, author):
        article = Article.objects.create(
            title=title,
            content=content,
            author=author
        )
        return article
    
    def publish_article(self, article):
        article.status = 'published'
        article.published_at = timezone.now()
        article.save()
        
        # Send notification
        notify_followers.delay(article.id)
        
        return article
```

### Service with Validation

```python
from django.core.exceptions import ValidationError

class ArticleService:
    def validate_article(self, title, content):
        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters long")
        if len(content) < 100:
            raise ValidationError("Content must be at least 100 characters long")
    
    def create_article(self, title, content, author):
        self.validate_article(title, content)
        
        article = Article.objects.create(
            title=title,
            content=content,
            author=author
        )
        return article
```

### Use Cases

- Complex business logic
- Transaction management
- Event handling
- Data validation

### Best Practices

- Keep services focused
- Use dependency injection
- Handle errors properly
- Document service methods

## Command Pattern

The command pattern encapsulates a request as an object.

### Basic Command

```python
class CreateArticleCommand:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def execute(self):
        article = Article.objects.create(
            title=self.title,
            content=self.content,
            author=self.author
        )
        return article
```

### Command with Validation

```python
class PublishArticleCommand:
    def __init__(self, article_id, publisher):
        self.article_id = article_id
        self.publisher = publisher
    
    def validate(self):
        if not self.publisher.has_permission('publish_article'):
            raise PermissionError("User does not have permission to publish")
    
    def execute(self):
        self.validate()
        
        article = Article.objects.get(id=self.article_id)
        article.status = 'published'
        article.published_at = timezone.now()
        article.publisher = self.publisher
        article.save()
        
        return article
```

### Use Cases

- Complex operations
- Undo/redo functionality
- Operation history
- Transaction management

### Best Practices

- Keep commands simple
- Validate input
- Handle errors
- Document command behavior

## Strategy Pattern

The strategy pattern defines a family of algorithms and makes them interchangeable.

### Basic Strategy

```python
from abc import ABC, abstractmethod

class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self, user, message):
        pass

class EmailNotification(NotificationStrategy):
    def notify(self, user, message):
        send_email(user.email, message)

class SMSNotification(NotificationStrategy):
    def notify(self, user, message):
        send_sms(user.phone, message)

class NotificationService:
    def __init__(self, strategy: NotificationStrategy):
        self.strategy = strategy
    
    def notify_user(self, user, message):
        self.strategy.notify(user, message)
```

### Use Cases

- Multiple algorithms
- Runtime configuration
- Plugin architecture
- Flexible behavior

### Best Practices

- Define clear interfaces
- Keep strategies focused
- Document strategy behavior
- Consider performance

## Observer Pattern

The observer pattern allows objects to be notified when events occur.

### Basic Observer

```python
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Article)
def notify_followers(sender, instance, created, **kwargs):
    if created:
        followers = instance.author.followers.all()
        for follower in followers:
            send_notification(
                follower,
                f"New article by {instance.author}: {instance.title}"
            )
```

### Custom Signal

```python
from django.dispatch import Signal, receiver

article_published = Signal()

class Article(models.Model):
    def publish(self):
        self.status = 'published'
        self.published_at = timezone.now()
        self.save()
        
        article_published.send(sender=self.__class__, instance=self)

@receiver(article_published)
def handle_article_published(sender, instance, **kwargs):
    # Update search index
    update_search_index.delay(instance.id)
    
    # Notify followers
    notify_followers.delay(instance.id)
```

### Use Cases

- Event handling
- Loose coupling
- Async operations
- Notifications

### Best Practices

- Use Django signals
- Keep handlers focused
- Handle errors
- Document signal behavior

## Repository Pattern

The repository pattern abstracts data access logic.

### Basic Repository

```python
class ArticleRepository:
    def get_by_id(self, article_id):
        return Article.objects.get(id=article_id)
    
    def get_published(self):
        return Article.objects.filter(status='published')
    
    def get_by_author(self, author):
        return Article.objects.filter(author=author)
    
    def save(self, article):
        article.save()
        return article
    
    def delete(self, article):
        article.delete()
```

### Repository with Caching

```python
from django.core.cache import cache

class CachedArticleRepository:
    def get_by_id(self, article_id):
        cache_key = f'article_{article_id}'
        article = cache.get(cache_key)
        
        if article is None:
            article = Article.objects.get(id=article_id)
            cache.set(cache_key, article, timeout=3600)
        
        return article
    
    def save(self, article):
        article.save()
        cache_key = f'article_{article.id}'
        cache.set(cache_key, article, timeout=3600)
        return article
```

### Use Cases

- Data access abstraction
- Caching strategy
- Query optimization
- Testing

### Best Practices

- Keep repositories focused
- Use meaningful method names
- Handle errors
- Consider caching

## Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Design Patterns Book](https://www.packtpub.com/product/django-design-patterns-and-best-practices/9781783986644)
- [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design) 