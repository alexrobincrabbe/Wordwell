from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import text

# Create your models here.

class UserProfile (models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null =True)
    profile_picture = CloudinaryField ('image', default = 'placeholder')
    about_me = models.TextField(null=True)
    join_date = models.DateTimeField(auto_now_add = True)
    display_name = models.CharField(max_length=20, unique=True, null=True)
    high_score = models.IntegerField(default=0)
    profile_url=models.SlugField(null = True)
    def save(self, *args, **kwargs):
        self.profile_url = text.slugify(self.user.username)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.user.username}'s Profile"


