# Form Patterns

This document covers common patterns used with Django forms, focusing on organizing form validation and processing effectively.

## Form Classes

Form classes are the basic building blocks for handling form data in Django.

### Basic Form

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from example.com domain")
        return email
```

### Use Cases

- Simple data collection
- Contact forms
- Search forms
- Data validation

### Best Practices

- Keep forms focused on a single purpose
- Use appropriate field types
- Implement custom validation when needed
- Use clean methods for field-specific validation
- Use clean for cross-field validation

## Model Forms

Model forms automatically create form fields based on model fields.

### Basic Model Form

```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
        }
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long")
        return title
```

### Use Cases

- CRUD operations
- Data editing
- Form generation from models
- Model validation

### Best Practices

- Specify fields explicitly
- Use widgets for custom rendering
- Implement custom validation when needed
- Use clean methods for field-specific validation
- Use clean for cross-field validation

## Form Mixins

Form mixins provide reusable functionality for forms through inheritance.

### TimeStampedForm Mixin

```python
class TimeStampedFormMixin:
    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.pk:  # New instance
            instance.created_at = timezone.now()
        instance.updated_at = timezone.now()
        if commit:
            instance.save()
        return instance
```

### UserForm Mixin

```python
class UserFormMixin:
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user = self.request.user
        if commit:
            instance.save()
        return instance
```

### Use Cases

- Shared functionality across forms
- Common validation logic
- Reusable form behavior

### Best Practices

- Keep mixins focused and single-purpose
- Document mixin behavior
- Consider mixin order
- Handle edge cases

## Form Wizards

Form wizards allow users to complete a multi-step form process.

### Basic Wizard

```python
from formtools.wizard.views import SessionWizardView
from django.shortcuts import render

class ArticleWizard(SessionWizardView):
    template_name = 'articles/wizard_form.html'
    
    def done(self, form_list, **kwargs):
        # Process all forms
        article_data = {}
        for form in form_list:
            article_data.update(form.cleaned_data)
        
        # Create article
        article = Article.objects.create(**article_data)
        return render(self.request, 'articles/wizard_done.html', {
            'article': article
        })
```

### Use Cases

- Multi-step forms
- Complex data collection
- Guided user input
- Form workflows

### Best Practices

- Keep steps focused and simple
- Provide clear navigation
- Save progress between steps
- Validate data at each step
- Provide a summary before completion

## Form Processing

Form processing patterns help organize the logic for handling form submissions.

### Basic Processing

```python
def process_form(request, form_class, template_name, success_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class()
    
    return render(request, template_name, {'form': form})
```

### Use Cases

- Consistent form handling
- Reusable form processing
- Standardized form responses

### Best Practices

- Keep processing logic separate from view logic
- Handle all form states (GET, POST, valid, invalid)
- Provide appropriate feedback
- Use messages framework for notifications

## Form Validation

Form validation patterns help organize the logic for validating form data.

### Basic Validation

```python
def validate_form(form):
    if not form.is_valid():
        return False, form.errors
    
    # Additional validation logic
    if form.cleaned_data['field1'] == form.cleaned_data['field2']:
        form.add_error('field2', 'Field 2 must be different from Field 1')
        return False, form.errors
    
    return True, None
```

### Use Cases

- Complex validation logic
- Cross-field validation
- Custom validation rules

### Best Practices

- Keep validation logic separate from form definition
- Use form methods for field-specific validation
- Use clean method for cross-field validation
- Provide clear error messages

## Resources

- [Django Forms Documentation](https://docs.djangoproject.com/en/5.0/topics/forms/)
- [Django Model Forms Documentation](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/)
- [Django Form Wizards Documentation](https://django-formtools.readthedocs.io/en/latest/) 