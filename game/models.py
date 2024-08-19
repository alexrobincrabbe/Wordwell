'''
Create models for game:
- scores
'''
from django.db import models
from profile_page.models import UserProfile


class Scores (models.Model):
    '''
    Stores all player scores:
    - Foreign Key: UserProfile
    '''
    profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="scores")
    score = models.IntegerField()

    def __str__(self):
        return f"{self.score} | Player: {self.profile.display_name}"
