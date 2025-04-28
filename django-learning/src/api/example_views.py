from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from .base_views import BaseListView, BaseDetailView, BaseCreateView, BaseUpdateView, BaseDeleteView
from .models import BlogPost
from .strategies import QueryStrategyFactory


class BlogPostListView(BaseListView):
    """List view for blog posts using the base view class."""
    model = BlogPost
    template_name = 'api/blog_post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        """Get the queryset based on the user's role using the strategy pattern."""
        strategy = QueryStrategyFactory.get_strategy(self.request.user)
        queryset = strategy.get_queryset()
        
        # Apply additional filtering if requested
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset


class BlogPostDetailView(BaseDetailView):
    """Detail view for blog post using the base view class."""
    model = BlogPost
    template_name = 'api/blog_post_detail.html'
    context_object_name = 'post'
    
    def get_object(self, queryset=None):
        """Get the blog post and increment view count."""
        obj = super().get_object(queryset)
        
        # Increment view count
        if hasattr(obj, 'view_count'):
            obj.view_count = obj.view_count + 1
            obj.save(update_fields=['view_count'])
        
        return obj


class BlogPostCreateView(LoginRequiredMixin, BaseCreateView):
    """Create view for blog post using the base view class."""
    model = BlogPost
    template_name = 'api/blog_post_form.html'
    success_url = reverse_lazy('blog_post_list')
    success_message = "Blog post '%(title)s' was created successfully"
    
    def pre_save(self, obj):
        """Set the author and slug before saving."""
        obj.author = self.request.user
        obj.slug = slugify(obj.title)


class BlogPostUpdateView(LoginRequiredMixin, BaseUpdateView):
    """Update view for blog post using the base view class."""
    model = BlogPost
    template_name = 'api/blog_post_form.html'
    success_url = reverse_lazy('blog_post_list')
    success_message = "Blog post '%(title)s' was updated successfully"
    
    def get_permission_required(self):
        """Check if the user is the author of the blog post."""
        post = self.get_object()
        if post.author != self.request.user:
            return 'api.change_blogpost'  # This will raise PermissionDenied
        return None
    
    def pre_save(self, obj):
        """Update the slug if the title changes."""
        if 'title' in self.request.POST and obj.title != self.get_object().title:
            obj.slug = slugify(obj.title)


class BlogPostDeleteView(LoginRequiredMixin, BaseDeleteView):
    """Delete view for blog post using the base view class."""
    model = BlogPost
    template_name = 'api/blog_post_confirm_delete.html'
    success_url = reverse_lazy('blog_post_list')
    success_message = "Blog post was deleted successfully"
    
    def get_permission_required(self):
        """Check if the user is the author of the blog post."""
        post = self.get_object()
        if post.author != self.request.user:
            return 'api.delete_blogpost'  # This will raise PermissionDenied
        return None 