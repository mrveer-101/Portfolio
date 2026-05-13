from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('blogs/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('portal/login/', views.custom_login, name='custom_login'),
    path('portal/logout/', views.custom_logout, name='custom_logout'),
    path('portal/dashboard/', views.dashboard, name='dashboard'),
    path('portal/blogs/', views.manage_blogs, name='manage_blogs'),
    path('portal/projects/', views.manage_projects, name='manage_projects'),
    path('portal/profile/', views.manage_profile, name='manage_profile'),
]
