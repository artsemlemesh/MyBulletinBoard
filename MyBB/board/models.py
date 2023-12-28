from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')#field 'through' improves query performance

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:post_detail', args=[str(self.id)])

class Category(models.Model):
    name = models.CharField(max_length=255, default='Name_of_category', unique=True)
    subscribers = models.ManyToManyField(User, blank=True, related_name='categories')
    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.category)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    status = models.BooleanField(default=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reaction on {self.author}\'s {self.post}'

    def get_absolute_url(self):
        return reverse('board:comment_detail', args=[str(self.id)])


class DisposableCode(models.Model):
    code = models.CharField(max_length=255, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=timezone.localtime(timezone.now() + timedelta(minutes=1)))

    def __str__(self):
        return f'disposable code: {self.code}'