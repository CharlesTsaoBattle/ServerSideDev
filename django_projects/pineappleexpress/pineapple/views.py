from django.shortcuts import render

# Create your views here.

#@login_required(login_url='/accounts/login/') # Redirected to login page if user first goes to home page
def home(request):
    """View function for home page of site."""
    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'home.html'
    )
