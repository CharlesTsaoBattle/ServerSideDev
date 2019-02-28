"""
urls.py
Created by Charles Tsao and Trent Williams
Last Updated: 01/03/2019
"""

from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

# Adds Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

# Product URLS
urlpatterns += [
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
]
