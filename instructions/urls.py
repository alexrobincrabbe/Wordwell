from . import views
from django.urls import path

urlpatterns =[
    path('', views.instructions, name="home"),
]