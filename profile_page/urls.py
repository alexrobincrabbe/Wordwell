'''
profile_page app urls
'''
from django.urls import path
from . import views

urlpatterns = [
    path('updateprofile/', views.update_user_profile, name="update_profile"),
    path('viewprofile/<str:target_profile>',
         views.view_user_profile, name="view_profile"),
]
