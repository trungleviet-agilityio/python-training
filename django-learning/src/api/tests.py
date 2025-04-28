from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from .models import BlogPost
import datetime


class BlogPostViewTests(TestCase):
    """Tests for blog post views."""
    
    def setUp(self):
        """Set up test data."""
        # Create users
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='password'
        )
        self.staff_user = User.objects.create_user(
            username='staff', email='staff@example.com', password='password', is_staff=True
        )
        self.author_user = User.objects.create_user(
            username='author', email='author@example.com', password='password'
        )
        self.regular_user = User.objects.create_user(
            username='user', email='user@example.com', password='password'
        )
        
        # Create blog posts
        self.published_post = BlogPost.objects.create(
            title='Published Post',
            slug='published-post',
            content='This is a published post.',
            author=self.author_user,
            status='published'
        )
        
        self.draft_post = BlogPost.objects.create(
            title='Draft Post',
            slug='draft-post',
            content='This is a draft post.',
            author=self.author_user,
            status='draft'
        )
        
        self.archived_post = BlogPost.objects.create(
            title='Archived Post',
            slug='archived-post',
            content='This is an archived post.',
            author=self.author_user,
            status='archived'
        )
        
        # Create a post with a specific date for archive tests
        self.dated_post = BlogPost.objects.create(
            title='Dated Post',
            slug='dated-post',
            content='This is a dated post.',
            author=self.author_user,
            status='published',
            created_at=timezone.now() - datetime.timedelta(days=30)
        )
    
    def test_blog_post_list_view_anonymous(self):
        """Test blog post list view for anonymous users."""
        client = Client()
        response = client.get(reverse('blog_post_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_list.html')
        self.assertContains(response, 'Published Post')
        self.assertNotContains(response, 'Draft Post')
    
    def test_blog_post_list_view_author(self):
        """Test blog post list view for author."""
        client = Client()
        client.login(username='author', password='password')
        response = client.get(reverse('blog_post_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_list.html')
        self.assertContains(response, 'Published Post')
        self.assertContains(response, 'Draft Post')
    
    def test_blog_post_list_view_staff(self):
        """Test blog post list view for staff."""
        client = Client()
        client.login(username='staff', password='password')
        response = client.get(reverse('blog_post_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_list.html')
        self.assertContains(response, 'Published Post')
        self.assertContains(response, 'Draft Post')
    
    def test_blog_post_list_view_admin(self):
        """Test blog post list view for admin."""
        client = Client()
        client.login(username='admin', password='password')
        response = client.get(reverse('blog_post_list'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_list.html')
        self.assertContains(response, 'Published Post')
        self.assertContains(response, 'Draft Post')
        self.assertContains(response, 'Archived Post')
    
    def test_blog_post_detail_view(self):
        """Test blog post detail view."""
        client = Client()
        response = client.get(reverse('blog_post_detail', args=['published-post']))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_detail.html')
        self.assertContains(response, 'Published Post')
        self.assertContains(response, 'This is a published post.')
    
    def test_blog_post_detail_view_increment_view_count(self):
        """Test that view count is incremented."""
        client = Client()
        initial_count = self.published_post.view_count
        
        response = client.get(reverse('blog_post_detail', args=['published-post']))
        self.published_post.refresh_from_db()
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.published_post.view_count, initial_count + 1)
    
    def test_blog_post_create_view_anonymous(self):
        """Test blog post create view for anonymous users."""
        client = Client()
        response = client.get(reverse('blog_post_create'))
        
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_blog_post_create_view_authenticated(self):
        """Test blog post create view for authenticated users."""
        client = Client()
        client.login(username='user', password='password')
        response = client.get(reverse('blog_post_create'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_form.html')
    
    def test_blog_post_create_view_post(self):
        """Test blog post create view POST request."""
        client = Client()
        client.login(username='user', password='password')
        
        response = client.post(
            reverse('blog_post_create'),
            {
                'title': 'New Post',
                'content': 'This is a new post.',
                'status': 'published'
            }
        )
        
        self.assertEqual(response.status_code, 302)  # Redirect to success URL
        self.assertTrue(BlogPost.objects.filter(slug='new-post').exists())
    
    def test_blog_post_update_view_anonymous(self):
        """Test blog post update view for anonymous users."""
        client = Client()
        response = client.get(reverse('blog_post_update', args=['published-post']))
        
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_blog_post_update_view_author(self):
        """Test blog post update view for author."""
        client = Client()
        client.login(username='author', password='password')
        response = client.get(reverse('blog_post_update', args=['published-post']))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_form.html')
    
    def test_blog_post_update_view_non_author(self):
        """Test blog post update view for non-author."""
        client = Client()
        client.login(username='user', password='password')
        response = client.get(reverse('blog_post_update', args=['published-post']))
        
        self.assertEqual(response.status_code, 403)  # Forbidden
    
    def test_blog_post_update_view_post(self):
        """Test blog post update view POST request."""
        client = Client()
        client.login(username='author', password='password')
        
        response = client.post(
            reverse('blog_post_update', args=['published-post']),
            {
                'title': 'Updated Post',
                'content': 'This is an updated post.',
                'status': 'published'
            }
        )
        
        self.assertEqual(response.status_code, 302)  # Redirect to success URL
        self.published_post.refresh_from_db()
        self.assertEqual(self.published_post.title, 'Updated Post')
        self.assertEqual(self.published_post.content, 'This is an updated post.')
    
    def test_blog_post_archive_view(self):
        """Test blog post archive view."""
        client = Client()
        response = client.get(reverse('blog_post_archive'))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_archive.html')
    
    def test_blog_post_year_archive_view(self):
        """Test blog post year archive view."""
        client = Client()
        year = timezone.now().year
        response = client.get(reverse('blog_post_year_archive', args=[year]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_year_archive.html')
    
    def test_blog_post_month_archive_view(self):
        """Test blog post month archive view."""
        client = Client()
        year = timezone.now().year
        month = timezone.now().month
        response = client.get(reverse('blog_post_month_archive', args=[year, month]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_month_archive.html')
    
    def test_blog_post_day_archive_view(self):
        """Test blog post day archive view."""
        client = Client()
        year = timezone.now().year
        month = timezone.now().month
        day = timezone.now().day
        response = client.get(reverse('blog_post_day_archive', args=[year, month, day]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api/blog_post_day_archive.html') 