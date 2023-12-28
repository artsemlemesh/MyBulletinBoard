from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', through='PostCategory')#field 'through' improves query performance

    def __str__(self):
        return f'{self.author}\'s post: {self.title} | {self.text}'


class Category(models.Model):
    name = models.CharField(max_length=255, default='Name_of_category', unique=True)

    def __str__(self):
        return self.name


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'post: {self.post}, category: {self.category}'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()
    status = models.BooleanField(default=False)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'author: {self.author}, comment: {self.comment_text}'