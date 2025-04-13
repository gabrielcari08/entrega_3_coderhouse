from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('authors/', views.authors, name="authors"),
    path('category/', views.category, name="category"),
    path('posts/', views.posts, name="posts"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)