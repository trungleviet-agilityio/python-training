from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BlogPost
from .serializers import BlogPostSerializer
from .strategies import QueryStrategyFactory
from .mixins import (
    AccessTrackingMixin, ViewCountMixin, CacheMixin, 
    CachePageMixin, LastModifiedMixin, AuthorRequiredMixin
)


# Function-Based View Example
def blog_post_detail(request, slug):
    """Function-based view for blog post detail."""
    post = get_object_or_404(BlogPost, slug=slug)
    post.increment_view_count()
    return render(request, 'api/blog_post_detail.html', {'post': post})


# Class-Based View Examples
class BlogPostListView(AccessTrackingMixin, CachePageMixin, ListView):
    """List view for blog posts."""
    model = BlogPost
    template_name = 'api/blog_post_list.html'
    context_object_name = 'posts'
    paginate_by = 10
    cache_timeout = 60 * 5  # 5 minutes
    
    def get_queryset(self):
        """Get the queryset based on the user's role using the strategy pattern."""
        strategy = QueryStrategyFactory.get_strategy(self.request.user)
        queryset = strategy.get_queryset()
        
        # Apply additional filtering if requested
        status_filter = self.request.GET.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset


# Date-based Archive Views
class BlogPostArchiveIndexView(AccessTrackingMixin, CachePageMixin, ArchiveIndexView):
    """Archive index view for blog posts."""
    model = BlogPost
    date_field = 'created_at'
    template_name = 'api/blog_post_archive.html'
    context_object_name = 'posts'
    make_object_list = True
    paginate_by = 10
    cache_timeout = 60 * 15  # 15 minutes
    
    def get_queryset(self):
        """Get the queryset based on the user's role using the strategy pattern."""
        strategy = QueryStrategyFactory.get_strategy(self.request.user)
        return strategy.get_queryset()


class BlogPostYearArchiveView(AccessTrackingMixin, CachePageMixin, YearArchiveView):
    """Year archive view for blog posts."""
    model = BlogPost
    date_field = 'created_at'
    template_name = 'api/blog_post_year_archive.html'
    context_object_name = 'posts'
    make_object_list = True
    paginate_by = 10
    cache_timeout = 60 * 30  # 30 minutes
    
    def get_queryset(self):
        """Get the queryset based on the user's role using the strategy pattern."""
        strategy = QueryStrategyFactory.get_strategy(self.request.user)
        return strategy.get_queryset()


class BlogPostMonthArchiveView(AccessTrackingMixin, CachePageMixin, MonthArchiveView):
    """Month archive view for blog posts."""
    model = BlogPost
    date_field = 'created_at'
    template_name = 'api/blog_post_month_archive.html'
    context_object_name = 'posts'
    make_object_list = True
    paginate_by = 10
    cache_timeout = 60 * 30  # 30 minutes
    
    def get_queryset(self):
        """Get the queryset based on the user's role using the strategy pattern."""
        strategy = QueryStrategyFactory.get_strategy(self.request.user)
        return strategy.get_queryset()


class BlogPostDayArchiveView(AccessTrackingMixin, CachePageMixin, DayArchiveView):
    """Day archive view for blog posts."""
    model = BlogPost
    date_field = 'created_at'
    template_name = 'api/blog_post_day_archive.html'
    context_object_name = 'posts'
    make_object_list = True
    paginate_by = 10
    cache_timeout = 60 * 30  # 30 minutes
    
    def get_queryset(self):
        """Get the queryset based on the user's role using the strategy pattern."""
        strategy = QueryStrategyFactory.get_strategy(self.request.user)
        return strategy.get_queryset()


class BlogPostDetailView(AccessTrackingMixin, ViewCountMixin, LastModifiedMixin, DetailView):
    """Detail view for blog post."""
    model = BlogPost
    template_name = 'api/blog_post_detail.html'
    context_object_name = 'post'
    
    def get_object(self, queryset=None):
        """Get the blog post and increment view count."""
        obj = super().get_object(queryset)
        return obj


class BlogPostCreateView(AccessTrackingMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Create view for blog post."""
    model = BlogPost
    template_name = 'api/blog_post_form.html'
    fields = ['title', 'content', 'status', 'featured_image']
    success_url = reverse_lazy('blog_post_list')
    success_message = "Blog post '%(title)s' was created successfully"
    
    def form_valid(self, form):
        """Set the author and slug."""
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class BlogPostUpdateView(AccessTrackingMixin, LoginRequiredMixin, AuthorRequiredMixin, SuccessMessageMixin, UpdateView):
    """Update view for blog post."""
    model = BlogPost
    template_name = 'api/blog_post_form.html'
    fields = ['title', 'content', 'status', 'featured_image']
    success_url = reverse_lazy('blog_post_list')
    success_message = "Blog post '%(title)s' was updated successfully"
    
    def form_valid(self, form):
        """Update the slug if the title changes."""
        if 'title' in form.changed_data:
            form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


# REST API ViewSet Example
class BlogPostViewSet(viewsets.ModelViewSet):
    """ViewSet for BlogPost model."""
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        """Get the queryset based on the user's role using the strategy pattern."""
        strategy = QueryStrategyFactory.get_strategy(self.request.user)
        queryset = strategy.get_queryset()
        
        # Apply additional filtering if requested
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset
    
    def perform_create(self, serializer):
        """Set the author and slug."""
        serializer.save(
            author=self.request.user,
            slug=slugify(serializer.validated_data['title'])
        )
    
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        """Publish a blog post."""
        post = self.get_object()
        post.publish()
        return Response({'status': 'post published'})
    
    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        """Archive a blog post."""
        post = self.get_object()
        post.archive()
        return Response({'status': 'post archived'}) 