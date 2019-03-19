from django.shortcuts import render
from django.views import generic
from .models import Product

# Create your views here.

#@login_required(login_url='/accounts/login/') # Redirected to login page if user first goes to home page
def home(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable.
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