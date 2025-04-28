from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Model
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .mixins import AccessTrackingMixin, CacheMixin, LastModifiedMixin


class BaseView(AccessTrackingMixin, View):
    """
    Base view class with template methods for common operations.
    """
    
    template_name = None
    model = None
    context_object_name = None
    success_url = None
    success_message = None
    permission_required = None
    
    def get_template_name(self):
        """Get the template name."""
        if self.template_name is None:
            raise NotImplementedError("template_name must be set")
        return self.template_name
    
    def get_model(self):
        """Get the model class."""
        if self.model is None:
            raise NotImplementedError("model must be set")
        return self.model
    
    def get_context_object_name(self):
        """Get the context object name."""
        if self.context_object_name is None:
            return self.get_model().__name__.lower()
        return self.context_object_name
    
    def get_success_url(self):
        """Get the success URL."""
        if self.success_url is None:
            raise NotImplementedError("success_url must be set")
        return self.success_url
    
    def get_success_message(self):
        """Get the success message."""
        return self.success_message
    
    def get_permission_required(self):
        """Get the permission required."""
        return self.permission_required
    
    def check_permissions(self):
        """Check if the user has the required permissions."""
        permission_required = self.get_permission_required()
        if permission_required and not self.request.user.has_perm(permission_required):
            raise PermissionDenied
    
    def get_context_data(self, **kwargs):
        """Get the context data."""
        context = kwargs
        context_object_name = self.get_context_object_name()
        if hasattr(self, 'object') and self.object is not None:
            context[context_object_name] = self.object
        return context
    
    def render_to_response(self, context):
        """Render the response."""
        return render(self.request, self.get_template_name(), context)
    
    def form_valid(self, form):
        """Handle a valid form."""
        self.object = form.save()
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        """Handle an invalid form."""
        return self.render_to_response(self.get_context_data(form=form))
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests."""
        self.check_permissions()
        return self.render_to_response(self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        """Handle POST requests."""
        self.check_permissions()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BaseListView(BaseView):
    """
    Base list view with template methods.
    """
    
    paginate_by = None
    paginate_orphans = 0
    allow_empty = True
    
    def get_queryset(self):
        """Get the queryset."""
        if not hasattr(self, 'queryset'):
            self.queryset = self.get_model().objects.all()
        return self.queryset
    
    def get_paginate_by(self):
        """Get the number of items to paginate by."""
        return self.paginate_by
    
    def get_paginate_orphans(self):
        """Get the number of orphans."""
        return self.paginate_orphans
    
    def get_allow_empty(self):
        """Get whether to allow empty lists."""
        return self.allow_empty
    
    def paginate_queryset(self, queryset, page_size):
        """Paginate the queryset."""
        paginator = Paginator(queryset, page_size, orphans=self.get_paginate_orphans())
        page_kwarg = 'page'
        page = self.request.GET.get(page_kwarg) or 1
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404("Page is not 'last', nor can it be converted to an int.")
        try:
            page = paginator.page(page_number)
        except EmptyPage:
            if self.get_allow_empty():
                page = paginator.page(paginator.num_pages)
            else:
                raise Http404("Empty list and %(class_name)s.allow_empty is False." % {
                    'class_name': self.__class__.__name__,
                })
        return (paginator, page, page.object_list, page.has_other_pages())
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests."""
        self.check_permissions()
        self.queryset = self.get_queryset()
        context_object_name = self.get_context_object_name()
        context = self.get_context_data()
        context[context_object_name] = self.queryset
        
        page_size = self.get_paginate_by()
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(self.queryset, page_size)
            context.update({
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                context_object_name: queryset,
            })
        
        return self.render_to_response(context)


class BaseDetailView(BaseView):
    """
    Base detail view with template methods.
    """
    
    def get_object(self, queryset=None):
        """Get the object."""
        if not hasattr(self, 'object'):
            model = self.get_model()
            pk = self.kwargs.get('pk')
            slug = self.kwargs.get('slug')
            
            if pk:
                self.object = model.objects.get(pk=pk)
            elif slug:
                self.object = model.objects.get(slug=slug)
            else:
                raise ValueError("Either pk or slug must be provided")
        
        return self.object
    
    def get(self, request, *args, **kwargs):
        """Handle GET requests."""
        self.check_permissions()
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data())
    
    def post(self, request, *args, **kwargs):
        """Handle POST requests."""
        self.check_permissions()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BaseCreateView(BaseView):
    """
    Base create view with template methods.
    """
    
    def get_form(self):
        """Get the form."""
        form_class = self.get_form_class()
        return form_class(self.request.POST or None)
    
    def get_form_class(self):
        """Get the form class."""
        if not hasattr(self, 'form_class'):
            from django import forms
            model = self.get_model()
            self.form_class = forms.modelform_factory(model, fields=self.get_form_fields())
        return self.form_class
    
    def get_form_fields(self):
        """Get the form fields."""
        if not hasattr(self, 'form_fields'):
            self.form_fields = [f.name for f in self.get_model()._meta.fields 
                               if f.name not in ['id', 'created_at', 'updated_at']]
        return self.form_fields
    
    def form_valid(self, form):
        """Handle a valid form."""
        self.object = form.save(commit=False)
        self.pre_save(self.object)
        self.object.save()
        form.save_m2m()
        self.post_save(self.object)
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return HttpResponseRedirect(self.get_success_url())
    
    def pre_save(self, obj):
        """Pre-save hook."""
        pass
    
    def post_save(self, obj):
        """Post-save hook."""
        pass


class BaseUpdateView(BaseView):
    """
    Base update view with template methods.
    """
    
    def get_object(self, queryset=None):
        """Get the object."""
        if not hasattr(self, 'object'):
            model = self.get_model()
            pk = self.kwargs.get('pk')
            slug = self.kwargs.get('slug')
            
            if pk:
                self.object = model.objects.get(pk=pk)
            elif slug:
                self.object = model.objects.get(slug=slug)
            else:
                raise ValueError("Either pk or slug must be provided")
        
        return self.object
    
    def get_form(self):
        """Get the form."""
        form_class = self.get_form_class()
        return form_class(self.request.POST or None, instance=self.get_object())
    
    def get_form_class(self):
        """Get the form class."""
        if not hasattr(self, 'form_class'):
            from django import forms
            model = self.get_model()
            self.form_class = forms.modelform_factory(model, fields=self.get_form_fields())
        return self.form_class
    
    def get_form_fields(self):
        """Get the form fields."""
        if not hasattr(self, 'form_fields'):
            self.form_fields = [f.name for f in self.get_model()._meta.fields 
                               if f.name not in ['id', 'created_at', 'updated_at']]
        return self.form_fields
    
    def form_valid(self, form):
        """Handle a valid form."""
        self.object = form.save(commit=False)
        self.pre_save(self.object)
        self.object.save()
        form.save_m2m()
        self.post_save(self.object)
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return HttpResponseRedirect(self.get_success_url())
    
    def pre_save(self, obj):
        """Pre-save hook."""
        pass
    
    def post_save(self, obj):
        """Post-save hook."""
        pass


class BaseDeleteView(BaseView):
    """
    Base delete view with template methods.
    """
    
    def get_object(self, queryset=None):
        """Get the object."""
        if not hasattr(self, 'object'):
            model = self.get_model()
            pk = self.kwargs.get('pk')
            slug = self.kwargs.get('slug')
            
            if pk:
                self.object = model.objects.get(pk=pk)
            elif slug:
                self.object = model.objects.get(slug=slug)
            else:
                raise ValueError("Either pk or slug must be provided")
        
        return self.object
    
    def delete(self, request, *args, **kwargs):
        """Delete the object."""
        self.object = self.get_object()
        self.pre_delete(self.object)
        self.object.delete()
        self.post_delete()
        success_message = self.get_success_message()
        if success_message:
            messages.success(self.request, success_message)
        return HttpResponseRedirect(self.get_success_url())
    
    def pre_delete(self, obj):
        """Pre-delete hook."""
        pass
    
    def post_delete(self):
        """Post-delete hook."""
        pass
    
    def post(self, request, *args, **kwargs):
        """Handle POST requests."""
        self.check_permissions()
        return self.delete(request, *args, **kwargs) 