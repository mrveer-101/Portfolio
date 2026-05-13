from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

def blog_detail(request, slug):
    # Currently a static template, slug is ignored for now but allows dynamic URLs later
    return render(request, 'blog_detail.html')

def project_detail(request, slug):
    return render(request, 'project_detail.html')

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
        
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('core:dashboard')
        else:
            return render(request, 'admin/login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'admin/login.html')

def custom_logout(request):
    logout(request)
    return redirect('core:index')

@login_required(login_url='core:custom_login')
def dashboard(request):
    return render(request, 'admin/dashboard.html')

@login_required(login_url='core:custom_login')
def manage_blogs(request):
    return render(request, 'admin/manage_blogs.html')

@login_required(login_url='core:custom_login')
def blog_create(request):
    return render(request, 'admin/blogs/create_blog.html')

@login_required(login_url='core:custom_login')
def blog_edit(request, slug):
    return render(request, 'admin/blogs/edit_blog.html', {'slug': slug})

@login_required(login_url='core:custom_login')
def blog_delete(request, slug):
    # In a real app, delete the model instance here.
    # We will just redirect back to manage_blogs.
    return redirect('core:manage_blogs')

@login_required(login_url='core:custom_login')
def blog_preview(request, slug):
    return render(request, 'admin/blogs/preview_blog.html', {'slug': slug})

@login_required(login_url='core:custom_login')
def manage_projects(request):
    return render(request, 'admin/manage_projects.html')

@login_required(login_url='core:custom_login')
def manage_profile(request):
    return render(request, 'admin/manage_profile.html')
