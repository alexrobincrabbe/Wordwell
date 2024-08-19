'''
Message_board app forms:
- PostForm
- ReplyForm
'''
from django import forms
from .models import Post, Reply


class PostForm(forms.ModelForm):
    '''
    Form to creat and edit posts
    '''
    class Meta:
        '''
        database model Post
        '''
        model = Post
        fields = ['title', 'text']


class ReplyForm(forms.ModelForm):
    '''
    Form to create and edit replies
    '''
    class Meta:
        '''
        database model Reply
        '''
        model = Reply
        fields = ['text']
