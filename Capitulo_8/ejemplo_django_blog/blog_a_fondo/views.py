from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView

from Capitulo_8.ejemplo_django_blog.blog_a_fondo.models import Category, Post



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created_at')[:100]


class CategoryListView(ListView):
    model = Category
