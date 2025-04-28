# Business Logic and Model Relationships

This document outlines the core business logic and model relationships for the Django project.

## Table of Contents

1. [Core Business Logic](#core-business-logic)
2. [Model Relationships](#model-relationships)
3. [Data Flow](#data-flow)
4. [Business Rules](#business-rules)
5. [User Roles and Permissions](#user-roles-and-permissions)

## Core Business Logic

### Blog System
- Users can create, edit, and delete blog posts
- Posts can be in draft or published state
- Only published posts are visible to the public
- Posts can be categorized and tagged
- Comments can be added to published posts
- Users can like/unlike posts

### User Management
- Users can register, login, and manage their profiles
- User profiles contain personal information and preferences
- Users can follow other users
- Users can receive notifications about interactions with their content

### Content Moderation
- New posts require approval before publication
- Comments can be flagged for inappropriate content
- Administrators can moderate content and user accounts

## Model Relationships

### User and Profile
```python
# One-to-One relationship
class User(AbstractUser):
    # Django's built-in user model
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### Blog Post and Related Models
```python
# Many-to-One relationship (Post to User)
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('pending', 'Pending Review'),
        ('published', 'Published'),
        ('rejected', 'Rejected'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='blog/', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    # Many-to-Many relationships
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    class Meta:
        ordering = ['-published_at', '-created_at']

# Many-to-Many relationship (Post to Category)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    
    class Meta:
        verbose_name_plural = 'categories'

# Many-to-Many relationship (Post to Tag)
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
```

### Comments and Interactions
```python
# Many-to-One relationship (Comment to Post and User)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['created_at']

# Many-to-One relationship (Like to Post and User)
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_records')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_records')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('post', 'user')
```

### User Following
```python
# Many-to-Many relationship (User to User)
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'following')
```

### Notifications
```python
# Many-to-One relationship (Notification to User)
class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ('like', 'Like'),
        ('comment', 'Comment'),
        ('follow', 'Follow'),
        ('mention', 'Mention'),
    )
    
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name='notifications')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
```

## Data Flow

### **Post Creation Flow**:
1. User creates a new post (status: draft)
2. User edits and previews the post
3. User submits for review (status: pending)
4. Moderator reviews the post
5. If approved, post is published (status: published)
6. If rejected, post returns to draft with feedback

- **Comment Flow**:
1. User comments on a published post
2. Comment is marked as unapproved
3. Moderator reviews the comment
4. If approved, comment is visible to all users
5. If rejected, comment is deleted

- **Notification Flow**:
1. User action triggers notification (like, comment, follow)
2. System creates notification record
3. Recipient receives notification
4. User marks notification as read

## Business Rules

### Content Rules
- Posts must have a title (5-200 characters)
- Posts must have content (minimum 100 characters)
- Posts can have up to 5 categories
- Posts can have up to 10 tags
- Comments must be at least 10 characters
- Users can edit their own comments within 24 hours

### User Rules
- Users must be 13+ years old to register
- Users can follow up to 1000 other users
- Users can block other users
- Users can report inappropriate content
- Users can delete their account (with 30-day recovery period)

### Moderation Rules
- New users' first 3 posts require approval
- Posts with flagged content are automatically set to pending
- Users with 3+ rejected posts are temporarily suspended
- Moderators must review flagged content within 24 hours

## User Roles and Permissions

### Regular User
- Create and manage own posts
- Comment on published posts
- Like/unlike posts
- Follow/unfollow other users
- Manage own profile
- Receive notifications

### Moderator
- All regular user permissions
- Approve/reject posts
- Approve/reject comments
- Flag inappropriate content
- Temporarily suspend users
- View moderation dashboard

### Administrator
- All moderator permissions
- Manage user accounts
- Manage categories and tags
- Configure site settings
- View analytics and reports
- Access admin interface 