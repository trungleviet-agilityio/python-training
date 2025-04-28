from django.db import models


class BlogPostManager(models.Manager):
    """
    Custom manager for BlogPost model with common query methods.
    """
    def published(self):
        """Return published blog posts."""
        return self.filter(status='published')
    
    def drafts(self):
        """Return draft blog posts."""
        return self.filter(status='draft')
    
    def archived(self):
        """Return archived blog posts."""
        return self.filter(status='archived')
    
    def by_author(self, author):
        """Return blog posts by a specific author."""
        return self.filter(author=author)
    
    def popular(self, limit=5):
        """Return the most viewed blog posts."""
        return self.filter(status='published').order_by('-view_count')[:limit]
    
    def recent(self, limit=5):
        """Return the most recent blog posts."""
        return self.filter(status='published').order_by('-created_at')[:limit] 