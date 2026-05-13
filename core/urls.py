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
]
