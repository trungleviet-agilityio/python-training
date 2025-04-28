# Template Patterns

This document covers common patterns used with Django templates, focusing on organizing template structure and rendering effectively.

## Template Inheritance

Template inheritance allows you to create a base template with common elements and extend it in child templates.

### Base Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Django Site{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{% url 'home' %}">Home</a></li>
                <li><a href="{% url 'about' %}">About</a></li>
                <li><a href="{% url 'contact' %}">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; {% now "Y" %} Django Site. All rights reserved.</p>
    </footer>
    
    <script src="{% static 'js/script.js' %}"></script>
</body>
</html>
```

### Child Template

```html
{% extends 'base.html' %}

{% block title %}Article Detail{% endblock %}

{% block content %}
    <article>
        <h1>{{ article.title }}</h1>
        <p class="meta">By {{ article.author }} on {{ article.published_at|date:"F j, Y" }}</p>
        
        <div class="content">
            {{ article.content|safe }}
        </div>
        
        <div class="tags">
            {% for tag in article.tags.all %}
                <span class="tag">{{ tag.name }}</span>
            {% endfor %}
        </div>
    </article>
{% endblock %}
```

### Use Cases

- Consistent site layout
- Reusable template elements
- DRY (Don't Repeat Yourself) principle
- Maintainable templates

### Best Practices

- Create a clear hierarchy of templates
- Use meaningful block names
- Keep blocks focused and specific
- Document template structure
- Use includes for small, reusable components

## Template Tags

Template tags allow you to add custom functionality to templates.

### Basic Template Tag

```python
from django import template

register = template.Library()

@register.simple_tag
def get_article_count(category):
    return Article.objects.filter(category=category).count()
```

### Template Tag with Context

```python
@register.inclusion_tag('articles/article_list.html')
def show_article_list(category, limit=5):
    articles = Article.objects.filter(category=category)[:limit]
    return {'articles': articles}
```

### Use Cases

- Reusable template logic
- Complex rendering logic
- Data formatting
- Conditional rendering

### Best Practices

- Keep template tags focused and simple
- Document template tag usage
- Use appropriate tag types (simple_tag, inclusion_tag)
- Consider performance implications

## Template Filters

Template filters allow you to modify variables in templates.

### Basic Filter

```python
@register.filter
def truncate_words(value, arg):
    words = value.split()
    if len(words) <= arg:
        return value
    return ' '.join(words[:arg]) + '...'
```

### Filter with Arguments

```python
@register.filter
def highlight(text, search_term):
    if not search_term:
        return text
    return text.replace(search_term, f'<span class="highlight">{search_term}</span>')
```

### Use Cases

- Text formatting
- Data transformation
- Conditional display
- String manipulation

### Best Practices

- Keep filters focused and simple
- Document filter usage
- Consider performance implications
- Use appropriate filter types

## Template Context Processors

Context processors add variables to the template context automatically.

### Basic Context Processor

```python
def site_settings(request):
    return {
        'SITE_NAME': 'Django Site',
        'SITE_DESCRIPTION': 'A Django-powered website',
    }
```

### Context Processor with Database Queries

```python
def navigation_menu(request):
    categories = Category.objects.all()
    return {
        'categories': categories,
    }
```

### Use Cases

- Global template variables
- Site-wide settings
- Navigation menus
- User information

### Best Practices

- Keep context processors focused
- Document context processor usage
- Consider performance implications
- Use caching for expensive operations

## Template Includes

Template includes allow you to include small, reusable template fragments.

### Basic Include

```html
{% include 'includes/header.html' %}

<main>
    {% block content %}
    {% endblock %}
</main>

{% include 'includes/footer.html' %}
```

### Include with Variables

```html
{% include 'includes/article_card.html' with article=article %}
```

### Use Cases

- Reusable template fragments
- Modular templates
- DRY principle
- Maintainable templates

### Best Practices

- Keep includes small and focused
- Use meaningful include names
- Document include usage
- Consider performance implications

## Template Organization

Template organization patterns help structure templates effectively.

### App-Based Organization

```
templates/
├── base.html
├── home.html
├── articles/
│   ├── list.html
│   ├── detail.html
│   └── form.html
└── users/
    ├── profile.html
    └── settings.html
```

### Feature-Based Organization

```
templates/
├── base.html
├── home.html
├── article_list.html
├── article_detail.html
├── article_form.html
├── user_profile.html
└── user_settings.html
```

### Use Cases

- Large projects
- Multiple developers
- Complex template structure
- Maintainable templates

### Best Practices

- Choose an organization strategy and stick to it
- Document template organization
- Use meaningful template names
- Consider project size and complexity

## Resources

- [Django Templates Documentation](https://docs.djangoproject.com/en/5.0/topics/templates/)
- [Django Template Tags Documentation](https://docs.djangoproject.com/en/5.0/ref/templates/builtins/)
- [Django Template Language Documentation](https://docs.djangoproject.com/en/5.0/ref/templates/language/) 