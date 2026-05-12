from django.shortcuts import render

def index(request):
    """
    Renders the main landing page of the portfolio.
    """
    return render(request, 'index.html')
