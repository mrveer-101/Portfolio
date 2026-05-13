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
    path('portal/blogs/create/', views.blog_create, name='blog_create'),
    path('portal/blogs/<slug:slug>/edit/', views.blog_edit, name='blog_edit'),
    path('portal/blogs/<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
    path('portal/blogs/<slug:slug>/preview/', views.blog_preview, name='blog_preview'),
    path('portal/projects/', views.manage_projects, name='manage_projects'),
    path('portal/projects/create/', views.project_create, name='project_create'),
    path('portal/projects/<slug:slug>/edit/', views.project_edit, name='project_edit'),
    path('portal/projects/<slug:slug>/delete/', views.project_delete, name='project_delete'),
    path('portal/projects/<slug:slug>/preview/', views.project_preview, name='project_preview'),
    path('portal/profile/', views.manage_profile, name='manage_profile'),
]
