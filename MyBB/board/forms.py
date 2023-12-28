from django import forms
from .models import Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=10, widget=CKEditorUploadingWidget()) # crucial field in uploading media, creates button upload
    class Meta:
        model = Post
        fields = ['title', 'text', 'category']





class CommentForm(forms.ModelForm):
    text = forms.CharField(min_length=10)
    class Meta:
        model = Comment
        fields = ['post', 'text']
