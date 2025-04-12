from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author, Category, Post

# Create your views here.

def home(request):
    return render(request, "base.html")

def authors(request):
    return render(request, "authors.html")

def category(request):
    return render(request, "category.html")

def posts(request):
    return render(request, 'posts.html')