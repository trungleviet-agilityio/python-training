from django.db import models
from django.conf import settings
from .managers import BlogPostManager


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created_at`` and ``updated_at`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogPost(TimeStampedModel):
    """
    A blog post model that demonstrates various model patterns.
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('published', 'Published'),
            ('archived', 'Archived'),
        ],
        default='draft'
    )
    featured_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)

    # Use the custom manager
    objects = BlogPostManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title

    def publish(self):
        """Publish the blog post."""
        self.status = 'published'
        self.save()

    def archive(self):
        """Archive the blog post."""
        self.status = 'archived'
        self.save()

    def increment_view_count(self):
        """Increment the view count."""
        self.view_count += 1
        self.save(update_fields=['view_count']) 