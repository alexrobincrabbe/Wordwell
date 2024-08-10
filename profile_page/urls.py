from . import views
from django.urls import path

urlpatterns =[
    path('updateprofile/', views.update_user_profile, name="update_profile"),
    path('viewprofile/<str:profile_view>', views.view_user_profile, name="view_profile"),
]