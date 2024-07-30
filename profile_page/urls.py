from . import views
from django.urls import path

urlpatterns =[
    path('profile/', views.display_user_profile, name="profile"),
    path('viewprofile/<str:profile_view>', views.view_user_profile, name="view_user_profile"),
]