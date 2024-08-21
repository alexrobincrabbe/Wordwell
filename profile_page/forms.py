'''
profile page app forms
'''
from django import forms
from django.contrib.auth.models import User
from cloudinary.forms import CloudinaryFileField
from .models import UserProfile


class UserUpdateForm(forms.ModelForm):
    '''
    Form to update user
    '''
    class Meta:
        '''
        Model User
        '''
        model = User
        fields = ['email']


class ProfileUpdateForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    about_me = forms.CharField(
        required=False, max_length=500,
        widget=forms.Textarea(attrs={"rows": "3"})
        )
    profile_picture = CloudinaryFileField(
        label="Profile Picture", required=False
        )
    display_name = forms.CharField(max_length=10)

    class Meta:
        '''
        Model UserProfile
        '''
        model = UserProfile
        fields = ['display_name', 'profile_picture', 'about_me']
