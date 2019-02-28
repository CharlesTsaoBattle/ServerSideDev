"""
views.py
Created by Charles Tsao and Trent Williams
Last Updated: 01/03/2019
"""
from django.shortcuts import render
from django.views import generic
from .models import Product

def home(request):
    """View function for home page of site."""
    # Render the HTML template home.html with the data in the context variable.
    return render(
        request,
        'home.html'
    )


class ProductListView(generic.ListView):
    """Generic class-based view for a list of products."""
    model = Product
    paginate_by = 10


class ProductDetailView(generic.DetailView):
    """Generic class-based detail view for a product."""
    model = Product
