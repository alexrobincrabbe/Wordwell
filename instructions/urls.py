'''
Instructions urls:
- home
'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.instructions, name="home"),
]
