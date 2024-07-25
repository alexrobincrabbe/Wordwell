from django.shortcuts import render, redirect, get_object_or_404
from dotenv import load_dotenv
load_dotenv()
import cloudinary
import cloudinary.uploader
import cloudinary.api
from .models import UserProfile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def display_user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    #user = request.user
    #profile = user.profile
    #if request.method == "POST":
    #    new_picture = request.POST['profile-pic-upload']
    
    return render(
        request,
        "profile_page/profile.html",
        context,
    )

def view_user_profile(request, profile_view):
    user_view = get_object_or_404(UserProfile.objects, profile_url=profile_view)
    return render(
        request,
        "profile_page/view_profile.html",
        {
            "user_view":user_view,
        }
    )

        