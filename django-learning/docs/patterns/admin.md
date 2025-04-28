# Admin Patterns

This document covers common patterns used with Django admin interface, focusing on customizing and extending the admin functionality.

## Basic Admin

The basic admin pattern registers models with minimal customization.

### Basic ModelAdmin

```python
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
```

### Use Cases

- Simple model administration
- Basic CRUD operations
- Quick prototypes
- Data management

### Best Practices

- Use meaningful list_display fields
- Add appropriate filters
- Enable search functionality
- Use date hierarchy for temporal data

## Advanced Admin

Advanced admin patterns provide more customization and functionality.

### Custom Actions

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    actions = ['make_published', 'make_draft']
    
    def make_published(self, request, queryset):
        updated = queryset.update(status='published')
        self.message_user(request, f'{updated} articles were published.')
    make_published.short_description = "Mark selected articles as published"
    
    def make_draft(self, request, queryset):
        updated = queryset.update(status='draft')
        self.message_user(request, f'{updated} articles were marked as draft.')
    make_draft.short_description = "Mark selected articles as draft"
```

### Custom List Display

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'comment_count']
    
    def comment_count(self, obj):
        return obj.comments.count()
    comment_count.short_description = 'Comments'
```

### Use Cases

- Complex model administration
- Bulk operations
- Custom functionality
- Advanced data management

### Best Practices

- Keep actions focused and simple
- Use clear action descriptions
- Handle errors gracefully
- Provide user feedback

## Inline Admin

Inline admin patterns allow editing related models in the same form.

### Basic Inline

```python
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
```

### Stacked Inline

```python
class MetadataInline(admin.StackedInline):
    model = Metadata
    can_delete = False
    max_num = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [MetadataInline]
```

### Use Cases

- Related model editing
- One-to-many relationships
- Many-to-many relationships
- Complex data structures

### Best Practices

- Choose appropriate inline type
- Set reasonable limits
- Consider form complexity
- Handle validation properly

## Admin Forms

Admin form patterns customize the edit and add forms in the admin.

### Custom Form

```python
from django import forms

class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'rows': 20}),
        }

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
```

### Fieldsets

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'content')
        }),
        ('Publishing', {
            'fields': ('status', 'published_at'),
            'classes': ('collapse',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        })
    )
```

### Use Cases

- Complex form layouts
- Custom validation
- Field grouping
- Advanced widgets

### Best Practices

- Group related fields
- Use appropriate widgets
- Implement validation
- Consider user experience

## Admin Views

Admin view patterns add custom views to the admin interface.

### Custom Admin View

```python
from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

class ArticleAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('statistics/', 
                 self.admin_site.admin_view(self.statistics_view),
                 name='article_statistics'),
        ]
        return custom_urls + urls
    
    def statistics_view(self, request):
        context = {
            **self.admin_site.each_context(request),
            'title': 'Article Statistics',
            'articles': Article.objects.all(),
        }
        return TemplateResponse(request, 'admin/article_statistics.html', context)
```

### Use Cases

- Custom reports
- Data visualization
- Complex operations
- Administrative tools

### Best Practices

- Use admin templates
- Handle permissions
- Provide navigation
- Consider security

## Admin Customization

Admin customization patterns modify the admin interface appearance and behavior.

### Custom Admin Site

```python
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'My Site Administration'
    site_title = 'My Site Admin'
    index_title = 'Welcome to My Site Admin'

admin_site = CustomAdminSite(name='custom_admin')
```

### Custom Templates

```python
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    change_form_template = 'admin/article/change_form.html'
    change_list_template = 'admin/article/change_list.html'
```

### Use Cases

- Branded admin interface
- Custom functionality
- Enhanced user experience
- Specialized workflows

### Best Practices

- Maintain admin look and feel
- Consider user familiarity
- Document customizations
- Test thoroughly

## Resources

- [Django Admin Documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/)
- [Django Admin Actions Documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/actions/)
- [Django Admin Site Documentation](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/#django.contrib.admin.AdminSite) 