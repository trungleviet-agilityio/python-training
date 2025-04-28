from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils import timezone
from django.db.models import F
import logging
import time

logger = logging.getLogger(__name__)


class AccessTrackingMixin:
    """
    Mixin to track access to views.
    Logs the user, view, and timestamp.
    """
    
    def dispatch(self, request, *args, **kwargs):
        """Track access to the view."""
        start_time = time.time()
        response = super().dispatch(request, *args, **kwargs)
        end_time = time.time()
        
        # Log access information
        user = request.user.username if request.user.is_authenticated else 'anonymous'
        view_name = self.__class__.__name__
        path = request.path
        method = request.method
        status_code = response.status_code
        duration = end_time - start_time
        
        logger.info(
            f"Access: user={user}, view={view_name}, path={path}, "
            f"method={method}, status={status_code}, duration={duration:.2f}s"
        )
        
        return response


class ViewCountMixin:
    """
    Mixin to track view counts for objects.
    Increments a view_count field on the model.
    """
    
    def get_object(self, queryset=None):
        """Get the object and increment its view count."""
        obj = super().get_object(queryset)
        
        # Increment view count
        if hasattr(obj, 'view_count'):
            obj.view_count = F('view_count') + 1
            obj.save(update_fields=['view_count'])
        
        return obj


class CacheMixin:
    """
    Mixin to add caching to views.
    """
    
    cache_timeout = 60 * 15  # 15 minutes by default
    
    def get_cache_timeout(self):
        """Get the cache timeout in seconds."""
        return self.cache_timeout
    
    def get_cache_key(self, *args, **kwargs):
        """Get a unique cache key for this view."""
        # Default implementation uses the URL path
        return f"view:{self.request.path}"
    
    def get(self, request, *args, **kwargs):
        """Get the response, using cache if available."""
        cache_key = self.get_cache_key(*args, **kwargs)
        response = cache.get(cache_key)
        
        if response is None:
            response = super().get(request, *args, **kwargs)
            cache.set(cache_key, response, self.get_cache_timeout())
        
        return response


class CachePageMixin:
    """
    Mixin to add page caching to views.
    Uses Django's cache_page decorator.
    """
    
    cache_timeout = 60 * 15  # 15 minutes by default
    
    @method_decorator(cache_page(cache_timeout))
    def dispatch(self, request, *args, **kwargs):
        """Apply caching to the view."""
        return super().dispatch(request, *args, **kwargs)


class LastModifiedMixin:
    """
    Mixin to add Last-Modified header to responses.
    """
    
    def get_last_modified(self):
        """Get the last modified time for the object."""
        if hasattr(self, 'object') and self.object is not None:
            if hasattr(self.object, 'updated_at'):
                return self.object.updated_at
            elif hasattr(self.object, 'created_at'):
                return self.object.created_at
        return None
    
    def dispatch(self, request, *args, **kwargs):
        """Add Last-Modified header to the response."""
        response = super().dispatch(request, *args, **kwargs)
        
        last_modified = self.get_last_modified()
        if last_modified:
            response['Last-Modified'] = last_modified.strftime('%a, %d %b %Y %H:%M:%S GMT')
        
        return response


class AuthorRequiredMixin(UserPassesTestMixin):
    """
    Mixin to check if the user is the author of the blog post.
    """
    
    def test_func(self):
        """Test if the user is the author of the blog post."""
        post = self.get_object()
        return post.author == self.request.user 