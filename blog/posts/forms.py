from django import forms
from .models import Author, Category, Post

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class PostsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'content', 'published_date', 'updated_date']