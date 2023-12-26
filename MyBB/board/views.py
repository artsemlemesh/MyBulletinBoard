from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm

class PostList(ListView):
    model = Post




class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'