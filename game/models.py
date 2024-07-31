from django.db import models
from django.contrib.auth.models import User
from profile_page.models import UserProfile

# Create your models here.

class Scores (models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="scores")
    score = models.IntegerField()
    def __str__(self):
        return f"{self.score} | Player: {self.profile.display_name}"

