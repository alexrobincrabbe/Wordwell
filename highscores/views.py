from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def highScores(request):
    user_list = User.objects.all().order_by('-profile__high_score')

    return render (
        request,
        "highscores/highscores.html",
        {
            "user_list": user_list
        },
    )