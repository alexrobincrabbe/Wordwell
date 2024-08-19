'''
High score app urls:
- url highscores
'''
from django.urls import path
from . import views

urlpatterns = [
    path('highscores/', views.high_scores, name="highscores"),
]
