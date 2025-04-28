from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for the BlogPostViewSet
router = DefaultRouter()
router.register(r'blog-posts', views.BlogPostViewSet)

# URL patterns for function-based and class-based views
urlpatterns = [
    # Blog post URLs
    path('blog/', views.BlogPostListView.as_view(), name='blog_post_list'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog/create/', views.BlogPostCreateView.as_view(), name='blog_post_create'),
    path('blog/<slug:slug>/edit/', views.BlogPostUpdateView.as_view(), name='blog_post_update'),
    
    # Date-based archive URLs
    path('blog/archive/', views.BlogPostArchiveIndexView.as_view(), name='blog_post_archive'),
    path('blog/<int:year>/', views.BlogPostYearArchiveView.as_view(), name='blog_post_year_archive'),
    path('blog/<int:year>/<int:month>/', views.BlogPostMonthArchiveView.as_view(), name='blog_post_month_archive'),
    path('blog/<int:year>/<int:month>/<int:day>/', views.BlogPostDayArchiveView.as_view(), name='blog_post_day_archive'),
    
    # Include the router URLs
    path('api/', include(router.urls)),
] 