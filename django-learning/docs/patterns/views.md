# View Patterns

This document covers common patterns used with Django views, focusing on organizing request handling and response generation effectively.

## Function-Based Views (FBVs)

Function-based views are the simplest way to handle HTTP requests in Django.

### Basic FBV

```python
from django.shortcuts import render, get_object_or_404
from .models import Article

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article
    })
```

### FBV with Form Handling

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ArticleForm

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Article created successfully.')
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm()
    
    return render(request, 'articles/create.html', {
        'form': form
    })
```

### Use Cases

- Simple CRUD operations
- Form handling
- Custom logic
- Quick prototypes

### Best Practices

- Keep views focused and simple
- Use appropriate shortcuts
- Handle form validation
- Implement proper error handling
- Use messages framework

## Class-Based Views (CBVs)

Class-based views provide a more object-oriented way to handle HTTP requests.

### Basic CBV

```python
from django.views.generic import DetailView
from .models import Article

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:3]
        return context
```

### CBV with Form Handling

```python
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article
from .forms import ArticleForm

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/create.html'
    success_url = reverse_lazy('article_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
```

### Use Cases

- Complex CRUD operations
- Reusable view logic
- Consistent behavior
- Built-in functionality

### Best Practices

- Use appropriate generic views
- Implement required methods
- Override when necessary
- Use mixins for shared functionality
- Document custom behavior

## View Mixins

View mixins provide reusable functionality for views through inheritance.

### Authentication Mixin

```python
from django.contrib.auth.mixins import UserPassesTestMixin

class AuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_author
    
    def handle_no_permission(self):
        messages.error(self.request, 'You must be an author to access this page.')
        return redirect('home')
```

### Context Mixin

```python
class CategoryContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
```

### Use Cases

- Shared functionality
- Common behavior
- Cross-cutting concerns
- Reusable logic

### Best Practices

- Keep mixins focused
- Document mixin behavior
- Consider mixin order
- Handle edge cases
- Test mixin functionality

## Template View Pattern

The template view pattern separates view logic from template rendering.

### Basic Template View

```python
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_articles'] = Article.objects.filter(
            is_featured=True
        )[:5]
        return context
```

### Use Cases

- Static pages
- Complex context data
- Reusable templates
- Consistent rendering

### Best Practices

- Keep templates focused
- Use template inheritance
- Implement context data
- Handle template errors
- Document template requirements

## View Decorators

View decorators provide a way to modify view behavior.

### Basic Decorator

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def author_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_author:
            messages.error(request, 'You must be an author to access this page.')
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
@author_required
def article_create(request):
    # View logic here
    pass
```

### Use Cases

- Authentication
- Permission checks
- Request modification
- Response modification
- Logging and monitoring

### Best Practices

- Keep decorators focused
- Document decorator behavior
- Consider decorator order
- Handle edge cases
- Test decorator functionality

## View Composition

View composition allows combining multiple views or view components.

### Basic Composition

```python
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class ArticleListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 10
    
    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
```

### Use Cases

- Complex view behavior
- Reusable components
- Consistent behavior
- Cross-cutting concerns

### Best Practices

- Keep composition clear
- Document composition behavior
- Consider composition order
- Handle edge cases
- Test composition functionality

## Resources

- [Django Views Documentation](https://docs.djangoproject.com/en/5.0/topics/http/views/)
- [Django Class-Based Views](https://docs.djangoproject.com/en/5.0/topics/class-based-views/)
- [Django View Decorators](https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-login-required-decorator) 