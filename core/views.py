from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blogs(request):
    return render(request, 'blogs.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def projects(request):
    return render(request, 'projects.html')
