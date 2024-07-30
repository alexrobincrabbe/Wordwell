from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Scores (models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="score")
    score = models.IntegerField()
    def __str__(self):
        return f"{self.score} | Player: {self.player}"

