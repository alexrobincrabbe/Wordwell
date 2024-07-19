from . import views
from django.urls import path

urlpatterns =[
    path('profile/', views.display_user_profile, name="profile"),
]