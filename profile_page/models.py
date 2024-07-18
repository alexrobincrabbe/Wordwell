from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class UserProfile (models.Model):
    profile_picture = CloudinaryField ('image', default = 'placeholder')
    about_me = models.TextField()
    join_date = models.DateTimeField(auto_now_add = True)
    Display_name = models.CharField(max_length=12, unique=True)
    high_score = models.IntegerField(default=0)

