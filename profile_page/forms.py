from django import forms
from django.contrib.auth.models import User
from  .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    #email = forms.EmailField()
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name','profile_picture', 'about_me']
