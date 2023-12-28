from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_update.html'





class CommentCreate(CreateView):
    form_class = CommentForm
    model = Comment
    template_name = 'comment_create.html'

class CommentDetail(DetailView):
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'


class CategoryListView(PostList):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_list'




