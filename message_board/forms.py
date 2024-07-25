from django import forms
from django.contrib.auth.models import User
from .models import Post, Reply

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']