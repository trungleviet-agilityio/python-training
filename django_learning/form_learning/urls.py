# products/urls.py
from django.urls import path
from form_learning import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add/', views.add_product, name='add_product'),
]
