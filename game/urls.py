"""
Game app urls
"""

from django.urls import path
from . import views


urlpatterns = [
    path('game/', views.game, name="game"),
    path('game/dictionary', views.dictionary, name="dictionary"),
]
