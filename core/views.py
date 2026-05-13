from django.shortcuts import render

def index(request):
    """
    Renders the main landing page of the portfolio.
    """
    return render(request, 'home.html')

def about(request):
    """
    Renders the About page.
    """
    return render(request, 'about.html')

def contact(request):
    """
    Renders the Contact page.
    """
    return render(request, 'contact.html')
