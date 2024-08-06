from . import views
from django.urls import path

urlpatterns =[
    path('highscores/', views.highScores, name="highscores"),
]