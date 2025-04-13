from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    
class Category(models.Model):
    name = models.CharField(max_length=100) #Nombre de la categoria
    description = models.TextField()
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField()
        
    def __str__(self):
        return self.title