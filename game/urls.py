from . import views
from django.urls import path

urlpatterns=[
    path('game/', views.game, name="game"),
    path('game/dictionary', views.dictionary, name="dictionary"),
]