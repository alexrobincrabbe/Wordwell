from django import forms
from django.contrib.auth.models import User
from  .models import UserProfile
from cloudinary.forms import CloudinaryFileField

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileUpdateForm(forms.ModelForm):
    about_me = forms.CharField(required=False, max_length=500, widget=forms.Textarea(attrs={"rows":"3"}))
    profile_picture = CloudinaryFileField(label="Profile Picture", required =False)
    class Meta:
        model = UserProfile
        fields = ['display_name','profile_picture', 'about_me']
