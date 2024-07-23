from django.db import models
from django.contrib.auth.models import User
from django.utils import text
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="board_posts")
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField(max_length=200, unique=True)
    slug = models.SlugField()
    created_on = models.DateTimeField (auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        self.slug = text.slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | posted by {self.author}"
    
class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="board_replies")
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies")
    text = models.TextField()
    created_on = models.DateTimeField (auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.text[:50]}"