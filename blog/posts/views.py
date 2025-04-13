from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Author, Category, Post
from .forms import AuthorForm, CategoryForm, PostsForm

# Create your views here.

def home(request):
    return render(request, "base.html")

def authors(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save() #Lo almacena en la base de datos
            return redirect('authors')
    else:
        form = AuthorForm()
        
    return render(request, "authors.html", {"form": form})

def category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    else:
        form = CategoryForm()
        
    return render(request, "category.html", {"form": form})

def posts(request):
    form = PostsForm(request.POST or None)

    # Obtener todos los autores y categorías para el navbar
    all_authors = Author.objects.all()
    all_categories = Category.objects.all()

    # Recuperar parámetros del filtro
    author_id = request.GET.get('author')
    category_id = request.GET.get('category')

    # Filtrar los posts
    posts = Post.objects.all()
    if author_id:
        posts = posts.filter(author_id=author_id)
    if category_id:
        posts = posts.filter(category_id=category_id)

    # Si se envió el formulario para agregar post
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('posts')

    return render(request, 'posts.html', {
        "form": form,
        "posts": posts,
        "all_authors": all_authors,
        "all_categories": all_categories
    })