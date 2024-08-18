from dotenv import load_dotenv
load_dotenv()
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile

# Create your views here.


@login_required
def update_user_profile(request):
    """
    Update a user's profile page
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            try:
                u_form.save()
                p_form.save()
                messages.success(request,f'Your account has been updated')        
            except ValueError as e: 
                context = {
                    'u_form': u_form,
                    'p_form': p_form,
                }
                return render(
                    request,
                    "profile_page/update_profile.html",
                    context,
                )
            user=request.user
            return HttpResponseRedirect(
                    reverse('view_profile', args=[user.profile.profile_url])
            )
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(
        request,
        "profile_page/update_profile.html",
        context,
    )

def view_user_profile(request, target_profile):
    """
    View a user's profile page
    """
    user_profile = get_object_or_404(UserProfile.objects, profile_url=target_profile)

    return render(
        request,
        "profile_page/view_profile.html",
        {
            "user_view":user_profile,
        }
    )

        