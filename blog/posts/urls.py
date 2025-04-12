from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('authors/', views.authors, name="authors"),
    path('category/', views.category, name="category"),
    path('posts/', views.posts, name="posts"),
]