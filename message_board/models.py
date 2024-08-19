'''
Models for message_board app
- Post
- Reply
'''
from django.db import models
from django.contrib.auth.models import User
from django.utils import text


class Post(models.Model):
    '''
    Post model:
    foreingkey - User
    '''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="board_posts")
    title = models.CharField(max_length=50, unique=True)
    text = models.TextField(max_length=1000)
    slug = models.SlugField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        '''
        order by created_on date descending
        '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | posted by {self.author}"


class Reply(models.Model):
    '''
    Reply model:
    foreign keys - User, Post
    '''
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="board_replies")
    original_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="replies")
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        '''
        order by created_on, ascending
        '''
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.text[:50]}"
